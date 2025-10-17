# 🧩 application/port/output/event_publisher_port.py

from abc import ABC, abstractmethod
from chatbot.domain.event.base_event import BaseEvent

# Explicación de requerimientos:
# REQ-05: Permite notificar eventos relacionados con los mensajes.
# REQ-11: Facilita la contextualización de la conversación mediante eventos.
# REQ-12: Los eventos pueden ser almacenados o enviados a sistemas externos para persistencia o auditoría.

class EventPublisherPort(ABC):
    """
    Puerto de salida que define cómo publicar eventos del sistema.
    """

    @abstractmethod
    def publish_event(self, event: BaseEvent) -> None:
        """
        Publica un evento al sistema o repositorio de eventos.
        """
        pass
