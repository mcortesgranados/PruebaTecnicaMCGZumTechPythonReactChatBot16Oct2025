# 🏢 domain/event/user_message_event.py

# Este archivo define un evento de mensaje enviado por el usuario.
# Explicación de requerimientos:
# REQ-05: Permite capturar y manipular los mensajes enviados por el usuario.
# REQ-11: Facilita la contextualización de la respuesta asociando un mensaje con su Response.
# REQ-12: Este evento puede ser enviado a un repositorio o adaptador para almacenamiento o procesamiento adicional.

from .base_event import BaseEvent
from ..model.message import Message

class UserMessageEvent(BaseEvent):
    """
    Evento que representa un mensaje enviado por el usuario al chatbot.
    """

    def __init__(self, message: Message, occurred_at=None):
        super().__init__(occurred_at)
        self.message = message
