# assignment-terrafrom-cicd

# AWS Data Platform Assignment

## Infrastructure Setup (Terraform)
- Provisions S3 bucket: `example-bucket`
- Deploys Lambda function: `example-lambda`
- Tracks source code checksum for re-deployment
- Configures Lambda environment variables

## Python Script (S3 Upload)
- Script uploads `sample.txt` to S3 using boto3
- Logs success/failure to console

## Dockerfile
- Builds Python 3.9 image with boto3 installed
- Runs the upload script

## CI/CD Pipeline (GitHub Actions)
- Trigger: On push to main
- Steps:
  - Builds Docker image
  - Runs container to test Python S3 upload

## SQL Query
- Generates product sales report for the previous month, ranked by total sales.

## Folder Structure
Refer to the repo layout for file placements.
