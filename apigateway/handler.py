import json
from sqsHandler import SqsHandler

def handler(event, context):
    
    msg = event['body'];
    sqs = SqsHandler('https://sqs.us-east-1.amazonaws.com/498552288851/SQS_principal_prod')
    sqs.send(msg)
    body = {
        "message": "a mensagem capturada foi: " + str(msg)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
