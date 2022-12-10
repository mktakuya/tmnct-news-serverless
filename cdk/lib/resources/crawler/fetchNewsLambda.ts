import {
  aws_iam as iam,
  aws_lambda as lambda,
  aws_events as events,
  aws_events_targets as targets,
  Duration,
} from 'aws-cdk-lib';
import { ManagedPolicy } from 'aws-cdk-lib/aws-iam';
import { CdkStack } from '../../cdk-stack';
import { StackProps } from '../../stack-props';

export const buildFetchNewsLambda = (stack: CdkStack, props: StackProps) => {
  const iamRole = new iam.Role(stack, `fetchNewsLambda-role-${props.stage}`, {
    roleName: `fetchNewsLambda-role-${props.stage}`,
    assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com'),
    managedPolicies: [
      ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSLambdaBasicExecutionRole'),
      ManagedPolicy.fromAwsManagedPolicyName('AmazonSSMReadOnlyAccess'),
    ],
  });

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
      ENV: props.stage,
      CREDENTIALS_KEY_PREFIX: props.credentialsKeyPrefix,
      NEWS_FEED_URL: props.newsFeedUrl,
      S3_BUCKET_NAME: props.s3BucketName,
    },
    role: iamRole,
  });
};

export const buildRuleForFetchNewsLambda = (stack: CdkStack, props: StackProps, lambdaFunction: lambda.Function) => {
  return new events.Rule(stack, `scheduleRuleForFetchNewsLambda-${props.stage}`, {
    schedule: events.Schedule.rate(Duration.minutes(3)),
    targets: [new targets.LambdaFunction(lambdaFunction)],
  });
};
