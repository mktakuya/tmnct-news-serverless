import {
  GetObjectCommand,
  S3Client,
  ListObjectsCommand,
} from "@aws-sdk/client-s3";
import { News } from "../models/news";
import { Readable } from "stream";

export const fetchAllNews = async () => {
  const s3 = new S3Client({ region: "ap-northeast-1" });
  const bucketName = process.env.S3_BUCKET_NAME || "tmnct-news-crawler-staging";

  const listObjectsCommand = new ListObjectsCommand({
    Bucket: bucketName,
  });
  const listObjectsResponse = await s3.send(listObjectsCommand);
  const contents = listObjectsResponse.Contents;
  if (!contents) {
    return [];
  }

  const keys = contents
    .map((content) => content.Key)
    .filter((key): key is string => typeof key === "string");

  const news = await Promise.all(
    keys.map(async (key) => {
      const getObjectCommand = new GetObjectCommand({
        Bucket: bucketName,
        Key: key,
      });
      const getObjectResponse = await s3.send(getObjectCommand);

      // S3との通信に失敗すると下記コードはエラーになるが、
      // getStaticPropsでエラーが発生してもページのビルドが失敗するだけなので、一旦S3を全面的に信頼する。
      const body = getObjectResponse.Body;
      const json = JSON.parse(await body!.transformToString());
      const item: News = json as News;

      return item;
    })
  );

  return news;
};
