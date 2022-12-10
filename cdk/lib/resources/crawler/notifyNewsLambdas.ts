import { aws_iam as iam, aws_lambda as lambda, Duration } from 'aws-cdk-lib';
import { CdkStack } from '../../cdk-stack';
import { StackProps } from '../../stack-props';
import { ManagedPolicy } from 'aws-cdk-lib/aws-iam';

const buildIamRoleForLambda = (stack: CdkStack, props: StackProps, lambdaFunctionName: string) => {
  return new iam.Role(stack, `${lambdaFunctionName}-role-${props.stage}`, {
    roleName: `${lambdaFunctionName}-role-${props.stage}`,
    assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
    managedPolicies: [
      ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaBasicExecutionRole'),
      ManagedPolicy.fromAwsManagedPolicyName('AmazonSSMReadOnlyAccess'),
    ],
  });
};

export const buildTweetNewsLambda = (stack: CdkStack, props: StackProps) => {
  const iamRole = buildIamRoleForLambda(stack, props, 'tweet-news-lambda');

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
    role: iamRole,
    environment: {
      ENV: props.stage,
      CREDENTIALS_KEY_PREFIX: props.credentialsKeyPrefix,
      TWITTER_CREDENTIALS_KEY_PREFIX: props.twitterCredentialsKeyPrefix,
    },
  });
};

export const buildEmailNewsLambda = (stack: CdkStack, props: StackProps) => {
  const iamRole = buildIamRoleForLambda(stack, props, 'email-news-lambda');

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
    role: iamRole,
    environment: {
      ENV: props.stage,
      CREDENTIALS_KEY_PREFIX: props.credentialsKeyPrefix,
    },
  });
};

export const buildPingToVercelLambda = (stack: CdkStack, props: StackProps) => {
  const iamRole = buildIamRoleForLambda(stack, props, 'ping-to-vercel-lambda');

  return new lambda.DockerImageFunction(stack, `ping-to-vercel-lambda-${props.stage}`, {
    functionName: `ping-to-vercel-lambda-${props.stage}`,
    code: lambda.DockerImageCode.fromImageAsset('./lambda/crawler', {
      cmd: ['notify_news_function.ping_to_vercel_handler'],
      buildArgs: {
        '--platform': 'linux/amd64',
      },
    }),
    timeout: Duration.seconds(30),
    memorySize: 128,
    role: iamRole,
    environment: {
      ENV: props.stage,
      CREDENTIALS_KEY_PREFIX: props.credentialsKeyPrefix,

      // TODO: twitterCredentials ではないので名前直すとかなんとかする
      VERCEL_CREDENTIALS_KEY_PREFIX: props.twitterCredentialsKeyPrefix,
    },
  });
};
