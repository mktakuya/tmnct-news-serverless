import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { StackProps } from './stack-props';

import { buildS3Bucket } from './resources/crawler/s3';
import { buildFetchNewsLambda } from './resources/crawler/fetchNewsLambda';

export class CdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: StackProps) {
    super(scope, id, props);

    const s3Bucket = buildS3Bucket(this, props);
    const fetchNewsLambda = buildFetchNewsLambda(this, props);
    s3Bucket.grantReadWrite(fetchNewsLambda);
  }
}
