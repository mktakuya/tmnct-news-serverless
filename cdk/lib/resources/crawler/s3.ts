import { aws_s3 as s3, RemovalPolicy } from 'aws-cdk-lib';
import { CdkStack } from '../../cdk-stack';
import { StackProps } from '../../stack-props';

export const buildS3Bucket = (stack: CdkStack, props: StackProps) => {
  return new s3.Bucket(stack, `tmnct-news-crawler-${props.stage}`, {
    bucketName: `tmnct-news-crawler-${props.stage}`,
    blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
    removalPolicy: RemovalPolicy.DESTROY,
    eventBridgeEnabled: true,
  });
};
