#Fila SQS Principal
resource "aws_sqs_queue" "sqs_principal" {
  name = "SQS_principal_${terraform.workspace}"
  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.sqs_dlq.arn
    maxReceiveCount     = 1
  })

  tags = {
    Environment = "${terraform.workspace}"
  }
}

data "aws_sqs_queue" "sqs_principal" {
  name = "SQS_principal_${terraform.workspace}"
}


#Fila SQS DLQ
resource "aws_sqs_queue" "sqs_dlq" {
  name = "SQS_DLQ_${terraform.workspace}"
  tags = {
    Environment = "${terraform.workspace}"
  }
}

data "aws_sqs_queue" "sqs_dlq" {
  name = "SQS_DLQ_${terraform.workspace}"
}

#Topico SNS
resource "aws_sns_topic" "sns_email" {
  name = "SNS_email_${terraform.workspace}"
  tags = {
    Environment = "${terraform.workspace}"
  }
}