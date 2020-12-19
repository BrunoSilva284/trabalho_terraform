#ARN da fila SQS principal
output "SQS_principal_ARN" {
  value = "${aws_sqs_queue.sqs_principal.arn}"
}

#URL da fila SQS principal
output "SQS_principal_URL" {
  value = "${data.aws_sqs_queue.sqs_principal.url}"
}

#ARN da fila SQS DLQ
output "SQS_DLQ_ARN" {
  value = "${aws_sqs_queue.sqs_dlq.arn}"
}

#URL da fila SQS DLQ
output "SQS_DLQ_URL" {
  value = "${data.aws_sqs_queue.sqs_dlq.url}"
}

#ARN do SNS
output "SNS_EMAIL_ARN" {
  value = "${aws_sns_topic.sns_email.arn}"
}