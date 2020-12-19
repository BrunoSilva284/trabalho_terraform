# Trabalho Final Cloud Computing & SRE

>  Documentação do Trabalho de Conclusão da Disciplina CLOUD COMPUTING & SRE  - Prof.: RAFAEL DE FREITAS BARBOSA

## Itens criados com Terraform:
* SQS Principal
* SQS DLQ
* SNS Email para fila DLQ
 
## Serverless:
* TODO


# Passos para rodar a aplicação
* Navegar para pasta do projeto terraform:
*  cd trabalho_terraform/terraform/S3
*  terraform plan
*  terraform apply -auto-approve
*  cd ..
*  terraform plan
*  terraform apply -auto-approve
*  terraform output -json > ../serverless/arns.json
