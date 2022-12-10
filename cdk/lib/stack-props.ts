import { StackProps as StackPropsType } from 'aws-cdk-lib';

export interface StackProps extends StackPropsType {
  readonly stage: string;
  readonly newsFeedUrl: string;
  readonly s3BucketName: string;
  readonly credentialsKeyPrefix: string;
  readonly twitterCredentialsKeyPrefix: string;
}
