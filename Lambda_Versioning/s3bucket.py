import logging
import boto3
import json
from botocore.exceptions import ClientError
def handler(event, context):
    #s3 = boto3.client('s3')
    s3 = boto3.resource('s3', region_name='us-east-1')
    s3.create_bucket(Bucket='whizlabs30452597')
    content="File uploaded by version 1"
    responses3 = s3.Object('whizlabs30452597', 'version1.txt').put(Body=content)
    print("uploading file completed")