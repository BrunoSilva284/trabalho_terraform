import json
from sqsHandler import SqsHandler
from env import Variables

def handler(event, context):
    env = Variables()    
    msg = event['body'];
    sqs = SqsHandler(env.get_sqs_consulta_url())
    sqs.send(msg)
    body = {
        "message": "a mensagem capturada foi: " + str(msg)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
