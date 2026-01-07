import boto3

session = boto3.Session(
    region_name="ap-south-2"
)

rekognition = session.client(
    "rekognition",
    endpoint_url="https://rekognition.ap-south-2.amazonaws.com"
)

bucket_name = "smart-street-images-megha"
image_name = "street_garbage.jpeg"

response = rekognition.detect_labels(
    Image={
        "S3Object": {
            "Bucket": bucket_name,
            "Name": image_name
        }
    },
    MaxLabels=10,
    MinConfidence=70
)

print("\nDetected objects:\n")
for label in response["Labels"]:
    print(label["Name"], ":", round(label["Confidence"], 2), "%")