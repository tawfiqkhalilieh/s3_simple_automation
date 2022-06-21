from settings import Config
import os
import boto3

s3 = boto3.client('s3',aws_access_key_id=Config.aws_access_key,aws_secret_access_key_id=Config.aws_secret_access_key)
for key in os.listdir:
    s3.upload_file(key,Config.upload_file__bucket,Config.upload_folder+str(key))
