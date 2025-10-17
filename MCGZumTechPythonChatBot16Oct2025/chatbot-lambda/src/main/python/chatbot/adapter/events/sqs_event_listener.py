# 🔌 adapter/💬 events/sqs_event_listener.py

import boto3
import json
from chatbot.application.port.output.event_publisher_port import EventPublisherPort

# Explicación de requerimientos:
# REQ-12: Permite recibir eventos relacionados con mensajes desde un repositorio externo (SQS de AWS).
# REQ-13: Comunicación segura mediante AWS SQS para integración entre servicios.
# REQ-15: Escalable, permite procesar eventos en cola de manera asíncrona.

class SQSEventListener:
    def __init__(self, queue_url: str, event_publisher: EventPublisherPort):
        self.sqs_client = boto3.client("sqs")
        self.queue_url = queue_url
        self.event_publisher = event_publisher

    def listen(self):
        """
        Escucha mensajes en la cola SQS y los publica a través del EventPublisherPort
        """
        try:
            messages = self.sqs_client.receive_message(
                QueueUrl=self.queue_url,
                MaxNumberOfMessages=10,
                WaitTimeSeconds=10
            ).get("Messages", [])

            for msg in messages:
                body = json.loads(msg["Body"])
                # Publica el evento al puerto de aplicación
                self.event_publisher.publish_event(body)

                # Borra el mensaje procesado
                self.sqs_client.delete_message(
                    QueueUrl=self.queue_url,
                    ReceiptHandle=msg["ReceiptHandle"]
                )

        except Exception as e:
            print(f"Error procesando eventos SQS: {e}")
