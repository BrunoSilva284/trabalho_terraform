from sqsHandler import SqsHandler
from env import Variables
import json


def handler(event, context):
    env = Variables()
    sqs = SqsHandler(env.get_sqs_consulta_url())
    
    #Do array de mensagens do tópico, recebe uma mensagem
    msgs = sqs.getMessage(10)
    
    if('Messages' in msgs and len(msgs['Messages'])>0):
        print("itens identificados para a impressao:")
        for msg in msgs['Messages']:
            print(msg['Body'])
            sqs.deleteMessage(msg['ReceiptHandle'])
    else:
        print("nao existem itens para a impressao..")
