from sqsHandler import SqsHandler
from env import Variables
import json
import boto3


def handler(event, context):
    env = Variables()
    sqs = SqsHandler(env.get_sqs_consulta_url())
    sns = boto3.client('sns')
    
    #Do array de mensagens do tópico, recebe uma mensagem
    mensagens = sqs.getMessage(1)
    
    if('Messages' in mensagens and len(mensagens['Messages'])>0):
        for msg in mensagens['Messages']:
            #Aqui deve enviar para o SNS e depois excluir
            sqs.deleteMessage(msg['ReceiptHandle'])
            # Publish a simple message to the specified SNS topic
            response = sns.publish(
            TopicArn=env.get_sns_dest_url(),    
            Message=msg['Body'],    
            )
            # Print out the response
            print(response)
    else:
        print("nao existem itens para enviar para o SNS")
