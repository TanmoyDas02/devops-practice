'''
This is a script to take backup from local to AWS S3 bucket. It uses the boto3 library to interact with AWS S3 service. 
The script will upload files from a specified local directory to a specified S3 bucket. 
It also includes error handling to manage exceptions that may occur during the upload process.
'''

import boto3

s3 = boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)
        
        
def create_bucket(s3, bucket_name, region):
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
    print("Bucket created successfully")
    
def upload_backup(s3, local_directory, bucket_name, key_name):
    data = open(local_directory, 'rb')  # binary me read hoga
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup uploaded successfully")
    
bucket_name = "python-for-devops-tanmoy-2026"
region = "ap-south-1"
file_name = "C:\\Users\\TANMOY\\OneDrive\\Documents\\DevOps\\Python\\backup_with_automation\\backups_practice\\backup_2026-05-16.tar.gz"
#show_buckets(s3)
#create_bucket(s3, "python-for-devops-tanmoy-2026", "ap-south-1")
upload_backup(s3, file_name, bucket_name, "backup_2026-05-16.tar.gz")