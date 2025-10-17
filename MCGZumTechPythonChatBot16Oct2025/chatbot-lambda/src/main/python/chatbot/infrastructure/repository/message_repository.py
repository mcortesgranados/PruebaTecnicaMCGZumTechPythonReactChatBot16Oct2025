
from typing import List
from chatbot.domain.model.message import Message

class MessageRepository:
    """
    Repositorio simple en memoria para mensajes.
    En producción, aquí iría la lógica de base de datos.
    """
    def __init__(self):
        self._messages = []

    def save_message(self, message: Message) -> Message:
        self._messages.append(message)
        return message
    
    def update_message(self, message):
        for i, m in enumerate(self._messages):
            if id(m) == id(message):
                self._messages[i] = message
                return
        # Si no existe, lo agregamos
        self._messages.append(message)


    def get_messages_by_user(self, user_id: str) -> List[Message]:
        return [msg for msg in self._messages if msg.user_id == user_id]
