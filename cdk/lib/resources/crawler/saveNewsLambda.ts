import { aws_lambda as lambda } from 'aws-cdk-lib';
import { CdkStack } from '../../cdk-stack';
import { StackProps } from '../../stack-props';

export const buildSaveNewsLambda = (stack: CdkStack, props: StackProps) => {
  return new lambda.Function(stack, `save-news-lambda-${props.stage}`, {
    functionName: `save-news-lambda-${props.stage}`,
    runtime: lambda.Runtime.PYTHON_3_9,
    handler: 'lambda_function.save_news_handler',
    code: lambda.Code.fromAsset('lambda/crawler'),
  });
};
