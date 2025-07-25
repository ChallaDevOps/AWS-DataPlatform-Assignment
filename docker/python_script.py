import boto3
import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def upload_file_to_s3(bucket_name, file_name, object_name=None):
    s3 = boto3.client('s3')
    try:
        if object_name is None:
            object_name = file_name
        s3.upload_file(file_name, bucket_name, object_name)
        logger.info(f"Successfully uploaded {file_name} to {bucket_name}/{object_name}")
    except Exception as e:
        logger.error(f"Failed to upload {file_name}: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    upload_file_to_s3('example-bucket-assignment', 'sample.txt')
