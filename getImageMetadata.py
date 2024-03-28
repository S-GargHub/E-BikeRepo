import boto3
import os
from datetime import datetime

s3 = boto3.client('s3', region_name='us-west-2')
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def save_metadata(key, size, upload_time):
    table.put_item(
        Item={
            'key': key,
            'size': size,
            'upload_time': upload_time
        }
    )
    
    return {
        'statusCode': 200,
        'body': f'Metadata saved for {key}'
    }
    

def lambda_handler(event, context):
    # Get the uploaded image from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Get metadata about the uploaded image
    response = s3.get_object(Bucket=bucket, Key=key)
    metadata = response['Metadata']
    content_length = response['ContentLength']
    last_modified = response['LastModified'].isoformat()
    
    # Save the metadata to DynamoDB
    save_metadata(key, content_length, last_modified)
