import { Box, Container } from "@chakra-ui/react";
import Head from "next/head";
import { ReactNode } from "react";

type Props = {
  children?: ReactNode;
  title?: string | null;
};

const baseTitle = "苫小牧高専News";

export function Layout({ children, title = null }: Props) {
  return (
    <div>
      <Head>
        <title>{title ? `${title} - ${baseTitle}` : baseTitle}</title>
        <meta charSet="utf-8" />
        <meta
          name="viewport"
          content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no"
        />
      </Head>

      <Container
        maxWidth="1200px"
        m="3rem auto 6rem"
        p="0.25rem 0.5rem"
        display={{ md: "flex" }}
      >
        <Box
          flexShrink={0}
          width={{ base: "100%", md: "75%" }}
          pr={{ base: "auto", md: "2rem" }}
          mb={{ base: "2rem", md: "auto" }}
          boxSizing="border-box"
        >
          {children}
        </Box>
      </Container>
    </div>
  );
}
