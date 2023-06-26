import json
import boto3
def lambda_handler(event, context):
    client=boto3.client("stepfunctions")
    response=client.start_execution(stateMachineArn="arn:aws:states:ap-south-1:056166221790:stateMachine:MyStateMachinetwocra")

    
    
    
