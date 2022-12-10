#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { CdkStack } from '../lib/cdk-stack';

const app = new cdk.App();

const stage = app.node.tryGetContext('stage');
const config = app.node.tryGetContext('config')[stage] || {};

new CdkStack(app, `tmnct-news-stack-${stage}`, {
  stage,
  stackName: `tmnct-news-stack-${stage}`,
  ...config,
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
