# 🔌 adapter/💬 events/sns_event_publisher_adapter.py

import boto3
import json
from chatbot.application.port.output.event_publisher_port import EventPublisherPort

# Explicación de requerimientos:
# REQ-12: Permite persistir eventos relacionados con mensajes en un repositorio externo (SNS de AWS).
# REQ-13: Exposición segura mediante la infraestructura de AWS para comunicación entre servicios.
# REQ-15: Escalable, permite publicar eventos a múltiples consumidores.

class SNSEventPublisherAdapter(EventPublisherPort):
    def __init__(self, topic_arn: str):
        self.sns_client = boto3.client("sns")
        self.topic_arn = topic_arn

    def publish_event(self, event: dict) -> bool:
        """
        Publica un evento a AWS SNS
        """
        try:
            response = self.sns_client.publish(
                TopicArn=self.topic_arn,
                Message=json.dumps(event)
            )
            return response.get("MessageId") is not None
        except Exception as e:
            print(f"Error publicando evento SNS: {e}")
            return False
