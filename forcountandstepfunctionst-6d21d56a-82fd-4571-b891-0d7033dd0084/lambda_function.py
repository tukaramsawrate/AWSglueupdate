import json
import boto3

#s3=boto3.client("s3")
def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('tstukaram')
    l=0
    
## Bucket to use
#bucket = s3.Bucket('my-bucket')

    for obj in bucket.objects.filter(Delimiter='/', Prefix='dept/'):
        
        l+=1
        
    l1=0
    for obj1 in bucket.objects.filter(Delimiter='/', Prefix='empf/'):
        
        l1+=1
    
    s3=boto3.client("stepfunctions")
    if l1==l:
        print("lambda will start 3rd function")
        invokelam=boto3.client("lambda")
        response=invokelam.invoke(FunctionName='forinvole',InvocationType="Event")
        
    
    
    
   
       
        
    
        
    
    
    
        
        
   
