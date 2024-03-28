# E-Bike Application - Upload image and manage metadata

## Overview
This project is a web application for an e-bike company, designed to facilitate the management of image uploads and metadata. It allows users to upload images to an AWS S3 bucket, and then stores the image metadata in an AWS DynamoDB table. The frontend is built with HTML and communicates with serverless lambda functions based on various triggers (API gateway and s3 upload)

## Features
- Image upload functionality through a web interface.
- Uploads image to AWS S3.
- Extracts metadata such as time_created, key etc and stores it in AWS DynamoDB.

## Technologies
- **Frontend:** HTML and Python
- **Backend:** Python, Serverless Lamda
- **Database:** AWS DynamoDB
- **Storage:** AWS S3
- **Testing:** Pytest
- **Authentication:** Cognito
- **Deployment:** CircleCI and AWS Amplify

### Prerequisites
- Python 3.x
- AWS account and configure IAM user with required permissions
- Flask
- Boto3
- Pytest (for testing)
