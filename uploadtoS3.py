import json
import boto3
import uuid

from base64 import b64decode

def lambda_handler(event, context):
    bucket_name = 'ebike--images'
    s3_client = boto3.client('s3')
    image_data = event['body']
    object_key = uuid.uuid4().hex
    
    missing_padding = len(image_data) % 4
    if missing_padding:
        image_data += '=' * (4 - missing_padding)
            
    decoded_image_data = b64decode(image_data)
    
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=object_key,
            Body=decoded_image_data
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Object uploaded successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error uploading object to S3: {str(e)}')
        }