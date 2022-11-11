import { aws_lambda as lambda } from 'aws-cdk-lib';
import { CdkStack } from '../../cdk-stack';
import { StackProps } from '../../stack-props';

export const buildFetchNewsLambda = (stack: CdkStack, props: StackProps) => {
  return new lambda.Function(stack, `fetch-news-lambda-${props.stage}`, {
    functionName: `fetch-news-lambda-${props.stage}`,
    runtime: lambda.Runtime.PYTHON_3_9,
    handler: 'lambda_function.fetch_news_handler',
    code: lambda.Code.fromAsset('lambda/crawler'),
  });
};
