import json
import boto3
import datetime
sqs = boto3.resource('sqs')
now = datetime.datetime.now()
client = boto3.client('sns')

dy = boto3.client('dynamodb')
table=dynamodb.Table('Price')

def save_to_bucket(event, context):
    AWS_BUCKET_NAME = 'nusrategg'
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(AWS_BUCKET_NAME)
    data = json.dumps(event)
    a=json.loads(data)
    
    client = boto3.client('dynamodb')
    table=dynamodb.Table('Price')
    
    bucket.put_object(
        ContentType='application/json',
        Key=datetime.datetime.now().isoformat() + '.json',
        Body=data
    )
        
    body = {
        "uploaded": "true",
        "bucket": AWS_BUCKET_NAME
    }
    return {
        "statusCode": 200,
        "body": a
    }

    


