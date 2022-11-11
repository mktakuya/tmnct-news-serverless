import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { StackProps } from './stack-props';

import { buildCrawler } from './resources/crawler';

export class CdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: StackProps) {
    super(scope, id, props);

    buildCrawler(this, props);
  }
}
