# 🧩 application/port/output/message_repository_port.py

from abc import ABC, abstractmethod
from chatbot.domain.model.message import Message

# Explicación de requerimientos:
# REQ-05: Permite guardar y consultar mensajes enviados por el usuario.
# REQ-11: Facilita la contextualización, ya que se puede recuperar el historial de mensajes.
# REQ-12: Se define la interfaz para cualquier repositorio persistente (archivo, DB, etc.).

class MessageRepositoryPort(ABC):
    """
    Puerto de salida que define las operaciones que debe implementar
    cualquier repositorio de mensajes.
    """

    @abstractmethod
    def save_message(self, message: Message) -> None:
        """
        Guarda un mensaje enviado por el usuario en el repositorio.
        """
        pass

    @abstractmethod
    def get_messages_by_user(self, user_id: str) -> list[Message]:
        """
        Recupera todos los mensajes asociados a un usuario.
        """
        pass
