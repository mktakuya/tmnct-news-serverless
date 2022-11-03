import { StackProps as StackPropsType } from 'aws-cdk-lib';

export interface StackProps extends StackPropsType {
  readonly stage: string;
  readonly bucketName: string;
}
