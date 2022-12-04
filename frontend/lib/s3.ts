import {
  GetObjectCommand,
  S3Client,
  ListObjectsCommand,
} from "@aws-sdk/client-s3";
import { News } from "../models/news";

export const fetchAllNews = async () => {
  // Vercel上では
  // AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY
  // という名前の環境変数を作れない。
  // そのため、 _FOR_ME というsuffixをつけている。
  // https://vercel.com/docs/concepts/limits/overview#reserved-variables
  const accessKeyId =
    process.env.AWS_ACCESS_KEY_ID_FOR_ME || process.env.AWS_ACCESS_KEY_ID || "";
  const secretAccessKey =
    process.env.AWS_SECRET_ACCESS_KEY_FOR_ME ||
    process.env.AWS_SECRET_ACCESS_KEY ||
    "";

  const s3 = new S3Client({
    region: "ap-northeast-1",
    credentials: {
      accessKeyId,
      secretAccessKey,
    },
  });
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
