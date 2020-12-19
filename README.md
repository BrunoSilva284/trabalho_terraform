# Trabalho Final Cloud Computing & SRE

>  Documentação do Trabalho de Conclusão da Disciplina CLOUD COMPUTING & SRE  - Prof.: RAFAEL DE FREITAS BARBOSA

## Visão Geral do sistema:
![img/visao-geral.JPG](img/visao-geral.JPG)

## Itens criados com Terraform:
* SQS Principal
* SQS DLQ
* SNS Email para fila DLQ
 
## Serverless:
* TODO
* Lambda sqs-to-sns


# Passos para rodar a aplicação:

* Realize o clone do seguinte repositório:
```sh
git clone https://github.com/BrunoSilva284/trabalho_terraform.git
```

* Navegar até a pasta do projeto terraform e iniciá-lo:
```sh
cd trabalho_terraform/terraform/
terraform init
```
* Nesse ponto é recomendado selecionar o workspace e guardar seu nome em uma variável:
```sh
terraform workspace new prod
wks=$(terraform workspace show)
```

* Navegar até a pasta do S3 e inicia-lo:
```sh
cd S3/
terraform init
terraform workspace new $wks
terraform plan
terraform apply -auto-approve
cd ..
```

* Iniciar as duas filas SQS e o SNS:

*OBS*: O último comando cria um arquivo com os ARNs e URLs dos serviços criados para uso posterior.

```sh
terraform plan
terraform apply -auto-approve
terraform output -json > ../serverless/arns-${wks}.json
cd ..
```

* Iniciar as aplicações serverless:
```sh
cd serverless/lambda-sqs-to-sns
virtualenv ~/venv
source ~/venv/bin/activate
pip3 install -r requirements.txt -t layer
sls deploy
sls invoke -l -f sqsHandler
```
