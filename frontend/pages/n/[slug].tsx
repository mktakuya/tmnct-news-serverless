import type { NextPage, GetStaticProps, GetStaticPaths } from "next";
import { useRouter } from "next/router";
import { Heading } from "@chakra-ui/react";

import { Layout } from "../../components/Layout";

import { News } from "../../models/news";
import { fetchAllNews } from "../../lib/s3";
import { useEffect } from "react";

type Props = {
  news: News | null;
};

const NewsPage: NextPage<Props> = (props) => {
  const router = useRouter();

  const { news } = props;

  useEffect(() => {
    router.replace(news?.url ?? "/").finally(() => {
      console.log(`Redirected to ${news?.url ?? "/"}`);
    });
  }, []);

  return (
    <Layout>
      <Heading>{news?.title}</Heading>
    </Layout>
  );
};

export default NewsPage;

export const getStaticPaths: GetStaticPaths = async () => {
  const news = await fetchAllNews();

  const paths = news.map((n) => `/n/${n.slug}`);

  return {
    paths,
    fallback: true,
  };
};

// TODO:  WebStormのバグでlintエラーになっている。
//        WebStormアップデート後にエラーにならないか再確認する
// @ts-ignore
export const getStaticProps: GetStaticProps<Props> = async ({ params }) => {
  if (params && params.slug) {
    const slug = params.slug as string;

    const news = await fetchAllNews();

    const targetNews = news.find((n) => n.slug === slug);

    return {
      props: {
        news: targetNews,
      },
    };
  } else {
    return {
      props: {
        news: null,
      },
    };
  }
};
