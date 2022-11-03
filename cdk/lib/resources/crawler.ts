import { CdkStack } from '../cdk-stack';
import { StackProps } from '../stack-props';
import { buildS3Bucket } from './crawler/s3';

export const buildCrawler = (stack: CdkStack, props: StackProps) => {
  buildS3Bucket(stack, props);
};
