import os

class Variables:
    def __init__(self):
        self.__sqs_consulta = os.environ.get('sqs_consulta', '')

    def get_sqs_consulta_url(self):
        return self.__sqs_consulta
