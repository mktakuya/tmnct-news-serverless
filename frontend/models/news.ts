export type News = {
  title: string;
  wp_pid: number;
  url: string;
  pubDate: string;
  category: "news" | "info" | "none";
  content: string;
  slug: string;
};
