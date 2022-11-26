import {
  aws_iam as iam,
  aws_stepfunctions as sfn,
  aws_stepfunctions_tasks as tasks,
  RemovalPolicy,
  aws_logs as logs,
  aws_s3 as s3,
  aws_events as events,
  aws_events_targets as targets,
  Duration,
} from 'aws-cdk-lib';
import { CdkStack } from '../../cdk-stack';
import { StackProps } from '../../stack-props';

export const buildCrawlerStateMachine = (stack: CdkStack, props: StackProps, bucket: s3.Bucket) => {
  const stepfunctionsLogGroupName = `/aws/vendedlogs/states/tmnct-news-crawler-${props.stage}`;
  const stepFunctionsLogGroup = new logs.LogGroup(stack, `stepfunctions-log-group-${props.stage}`, {
    logGroupName: stepfunctionsLogGroupName,
    removalPolicy: RemovalPolicy.DESTROY,
  });

  const fetchNewsContentTask = new tasks.CallAwsService(stack, `fetch-news-content-task-${props.stage}`, {
    service: 's3',
    action: 'getObject',
    parameters: {
      Bucket: bucket.bucketName,
      Key: sfn.JsonPath.stringAt('$.object.key'),
    },
    iamResources: [`${bucket.bucketArn}/*`],
    outputPath: '$.Body',
  });

  const definition = fetchNewsContentTask;

  const stateMachine = new sfn.StateMachine(stack, `crawlerStateMachine-${props.stage}`, {
    definition,
    logs: {
      destination: stepFunctionsLogGroup,
    },
    timeout: Duration.minutes(5),
  });

  bucket.grantRead(stateMachine);

  return stateMachine;
};

export const buildRuleForCrawlerStateMachine = (
  stack: CdkStack,
  props: StackProps,
  stateMachine: sfn.StateMachine,
  bucket: s3.Bucket
) => {
  return new events.Rule(stack, `ruleForCrawlerStateMachine-${props.stage}`, {
    eventPattern: {
      source: ['aws.s3'],
      detailType: ['Object Created'],
      resources: [bucket.bucketArn],
    },
    targets: [
      new targets.SfnStateMachine(stateMachine, {
        input: events.RuleTargetInput.fromObject({
          object: {
            bucketName: events.EventField.fromPath('$.detail.bucket.name'),
            key: events.EventField.fromPath('$.detail.object.key'),
          },
        }),
      }),
    ],
  });
};
