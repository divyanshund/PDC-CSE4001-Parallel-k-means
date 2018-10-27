import boto3

bucketName = "cse4001"
Key = "/home/sai/Downloads/red.csv"
outPutname = "screenshot"

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)
import botocore

Bucket = "cse4001"
Key = "/home/sai/Pictures/a.png"
outPutname = "screenshot"

s3 = boto3.resource('s3')
try:
    s3.Bucket(Bucket).download_file(Key,outPutName)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise