import json

# import requests


def lambda_handler(event, context):


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Happy weekend!",
            # "location": ip.text.replace("\n", "")
        }),
    }
