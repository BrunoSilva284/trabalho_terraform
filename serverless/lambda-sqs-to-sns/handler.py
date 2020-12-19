from sqsHandler import SqsHandler
from env import Variables
import json


def handler(event, context):
    env = Variables()
    sqs = SqsHandler(env.get_sqs_consulta_url())
    
    #Do array de mensagens do tópico, recebe uma mensagem
    mensagens = sqs.getMessage(1)
    print(str(mensagens))
    
    #Itera o array e deleta ela do tópico usando o ReceiptHandle
    for msg in mensagens['Messages']:
        sqs.deleteMessage(msg['ReceiptHandle'])