import json
import boto3
import os

SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event, context):
    try:
        
        if 'body' in event:
            event = json.loads(event['body'])

        nume = event['nume']
        intrebari = event['intrebari']

        mesaj = f"Completed by: {nume}\nResponses:\n"
        for key, val in intrebari.items():
            mesaj += f"{key}: {val}\n"

        sns = boto3.client('sns')
        response = sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=mesaj,
            Subject="Another email with a candidate that applied"
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "E-mail sent!"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
