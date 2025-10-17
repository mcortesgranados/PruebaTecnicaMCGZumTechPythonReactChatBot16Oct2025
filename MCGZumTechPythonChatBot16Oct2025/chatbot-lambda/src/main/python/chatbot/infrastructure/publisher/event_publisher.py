class EventPublisher:
    """
    Publicador de eventos simple.
    En producción, podría enviar a Kafka, SQS, etc.
    """
    def publish(self, event_name: str, payload: dict):
        print(f"[EventPublisher] Evento '{event_name}' publicado con payload: {payload}")
    """
    Publicador de eventos en memoria.
    En producción aquí podrías integrar Kafka, SQS, etc.
    """
    def publish_event(self, event: dict):
        # Por ahora solo imprime el evento en consola
        print("Evento publicado:", event)        
