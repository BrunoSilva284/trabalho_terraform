from sqsHandler import SqsHandler
from env import Variables
import json


def handler(event, context):
    env = Variables()
    sqs = SqsHandler(env.get_sqs_consulta_url())
    
    #Do array de mensagens do tópico, recebe uma mensagem
    mensagens = sqs.getMessage(1)
    
    if('Messages' in mensagens and len(mensagens['Messages'])>0):
        for msg in mensagens['Messages']:
            #Aqui deve enviar para o SNS e depois excluir
            sqs.deleteMessage(msg['ReceiptHandle'])
    else:
        print("nao existem itens para enviar para o SNS")
