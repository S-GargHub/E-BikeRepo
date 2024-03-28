# E-Bike Application - Upload image and manage metadata

## Overview
This project was designed to seamlessly integrate a web application with various AWS services, facilitating image upload, metadata extraction, and storage. I used S3 for secure and reliable image storage, DynamoDB as a key-value pair database to house metadata, IAM roles to manage access permissions, and Lambda functions to execute code triggered by events such as image uploads.

## Features
- Image upload functionality through a web interface.
- Uploads image to AWS S3.
- Extracts metadata such as time_created, key etc and stores it in AWS DynamoDB.

## AWS Services Used
- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- IAM Roles
- Lambda function
- AWS Amplify
- AWS Cognito

### Prerequisites
- Python 3.x
- AWS account
- Flask
- Boto3
- Pytest (for testing)
- CircleCI
