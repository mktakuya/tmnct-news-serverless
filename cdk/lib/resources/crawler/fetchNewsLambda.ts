import {aws_lambda as lambda, aws_events as events, aws_events_targets as targets, Duration} from 'aws-cdk-lib';
import { CdkStack } from '../../cdk-stack';
import { StackProps } from '../../stack-props';

export const buildFetchNewsLambda = (stack: CdkStack, props: StackProps) => {
  return new lambda.DockerImageFunction(stack, `fetchNewsLambda-${props.stage}`, {
    functionName: `fetchNewsLambda-${props.stage}`,
    code: lambda.DockerImageCode.fromImageAsset('./lambda/crawler', {
      cmd: ['fetch_news_function.handler'],
      buildArgs: {
        '--platform': 'linux/amd64',
      },
    }),
    timeout: Duration.seconds(30),
    memorySize: 128,
    environment: {
      NEWS_FEED_URL: props.newsFeedUrl,
      S3_BUCKET_NAME: props.s3BucketName,
    },
  });
};

export const buildRuleForFetchNewsLambda = (stack: CdkStack, props: StackProps, lambdaFunction: lambda.Function) => {
  return new events.Rule(stack, `scheduleRuleForFetchNewsLambda-${props.stage}`, {
    schedule: events.Schedule.rate(Duration.minutes(3)),
    targets: [new targets.LambdaFunction(lambdaFunction)],
  })
}