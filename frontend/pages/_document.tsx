import Document, { Html, Head, Main, NextScript } from "next/document";

class CustomDocument extends Document {
  render() {
    return (
      <Html>
        <Head>{/*  TODO: GAの設定をする */}</Head>

        <body style={{ backgroundColor: "rgb(250, 249, 245)" }}>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}

export default CustomDocument;
