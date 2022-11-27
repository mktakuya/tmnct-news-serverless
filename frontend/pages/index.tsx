import type { NextPage } from "next";
import { Heading, Link, Divider, Text } from "@chakra-ui/react";
import { Layout } from "../components/Layout";
import { ExternalLinkIcon } from "@chakra-ui/icons";

const Home: NextPage = () => {
  return (
    <Layout>
      <Heading>苫小牧高専News</Heading>

      <Divider mb={"1rem"} />

      <Text>苫小牧高専のニュースをTwitterでお届け。</Text>

      <Text>
        <Link href={"https://twitter.com/TmNCT_News"} isExternal>
          @TmNCT_News <ExternalLinkIcon mx="2px" textAlign={"center"} />
        </Link>
      </Text>
    </Layout>
  );
};

export default Home;
