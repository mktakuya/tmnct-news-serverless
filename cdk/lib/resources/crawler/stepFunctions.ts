import {
  aws_logs as logs,
  aws_stepfunctions as stepfunctions,
  aws_stepfunctions_tasks as tasks,
  RemovalPolicy,
  Duration,
} from 'aws-cdk-lib';
import { CdkStack } from '../../cdk-stack';
import { StackProps } from '../../stack-props';

import { buildFetchNewsLambda } from './fetchNewsLambda';
import { buildSaveNewsLambda } from './saveNewsLambda';
import { buildTweetNewsLambda } from './tweetNewsLambda';

export const buildStepFunctions = (stack: CdkStack, props: StackProps) => {
  const fetchNewsLambda = buildFetchNewsLambda(stack, props);
  const saveNewsLambda = buildSaveNewsLambda(stack, props);
  const tweetNewsLambda = buildTweetNewsLambda(stack, props);

  // StepFunctionsのロググループ名は、 /aws/vendedlogs/states/ から始まるらしい
  // https://docs.aws.amazon.com/step-functions/latest/dg/bp-cwl.html
  const stepfunctionsLogGroupName = `/aws/vendedlogs/states/tmnct-news-crawler-${props.stage}`;
  const stepFunctionsLogGroup = new logs.LogGroup(stack, `stepfunctions-log-group-${props.stage}`, {
    logGroupName: stepfunctionsLogGroupName,
    removalPolicy: RemovalPolicy.DESTROY,
  });

  const fetchNewsTask = new tasks.LambdaInvoke(stack, `fetch-news-task-${props.stage}`, {
    lambdaFunction: fetchNewsLambda,
    outputPath: '$.Payload',
  });

  const saveNewsTask = new tasks.LambdaInvoke(stack, `save-news-task-${props.stage}`, {
    lambdaFunction: saveNewsLambda,
    outputPath: '$.Payload',
  });

  const tweetNewsTask = new tasks.LambdaInvoke(stack, `tweet-news-task-${props.stage}`, {
    lambdaFunction: tweetNewsLambda,
    outputPath: '$.Payload',
  });

  const saveAndTweetParallel = new stepfunctions.Parallel(stack, `parallel-${props.stage}`);
  saveAndTweetParallel.branch(saveNewsTask);
  saveAndTweetParallel.branch(tweetNewsTask);

  const terminalState = new stepfunctions.Pass(stack, `terminal-state-${props.stage}`);

  const definition = fetchNewsTask.next(
    new stepfunctions.Choice(stack, 'Is Updated?')
      .when(stepfunctions.Condition.isBoolean('$.updated'), saveAndTweetParallel)
      .otherwise(terminalState)
  );

  return new stepfunctions.StateMachine(stack, `stepfunctions-${props.stage}`, {
    definition,
    logs: {
      destination: stepFunctionsLogGroup,
    },
    timeout: Duration.minutes(5),
  });
};
