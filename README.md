# aws-rekognition-image-analysis
Image Analysis Project using AWS Rekognition and Amazon S3


# AWS Rekognition Image Analysis

This project demonstrates how to use Amazon Rekognition to analyze images stored in Amazon S3 and detect objects such as people and vehicles.

## Services Used
- Amazon S3
- Amazon Rekognition
- AWS CloudShell
- Python (Boto3 SDK)

## How It Works
1. An image is uploaded to an S3 bucket in the Mumbai (ap-south-1) region.
2. A Python script uses the AWS Boto3 SDK to call Amazon Rekognition.
3. Rekognition analyzes the image and returns detected object labels with confidence scores.
4. The results are printed in the terminal.

## Sample Output
- Person
- Adult
- Vehicle
- Car

## Region Note
Amazon Rekognition is currently supported in ap-south-1 (Mumbai). The project was configured accordingly.

## Author
Megha Dinesh
