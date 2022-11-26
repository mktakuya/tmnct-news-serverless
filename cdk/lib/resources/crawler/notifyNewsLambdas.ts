import { aws_lambda as lambda, Duration } from 'aws-cdk-lib';
import { CdkStack } from '../../cdk-stack';
import { StackProps } from '../../stack-props';

export const buildTweetNewsLambda = (stack: CdkStack, props: StackProps) => {
  return new lambda.DockerImageFunction(stack, `tweet-news-lambda-${props.stage}`, {
    functionName: `tweet-news-lambda-${props.stage}`,
    code: lambda.DockerImageCode.fromImageAsset('./lambda/crawler', {
      cmd: ['notify_news_function.tweet_news_handler'],
      buildArgs: {
        '--platform': 'linux/amd64',
      },
    }),
    timeout: Duration.seconds(30),
    memorySize: 128,
    environment: {},
  });
};

export const buildEmailNewsLambda = (stack: CdkStack, props: StackProps) => {
  return new lambda.DockerImageFunction(stack, `email-news-lambda-${props.stage}`, {
    functionName: `email-news-lambda-${props.stage}`,
    code: lambda.DockerImageCode.fromImageAsset('./lambda/crawler', {
      cmd: ['notify_news_function.email_news_handler'],
      buildArgs: {
        '--platform': 'linux/amd64',
      },
    }),
    timeout: Duration.seconds(30),
    memorySize: 128,
    environment: {},
  });
};
