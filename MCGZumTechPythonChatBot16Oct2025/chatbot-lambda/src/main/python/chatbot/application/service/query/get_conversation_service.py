# 🧩 application/service/query/get_conversation_service.py

from typing import List
from chatbot.application.port.output.message_repository_port import MessageRepositoryPort
from chatbot.domain.model.message import Message

# Explicación de requerimientos:
# REQ-05: Permite recuperar mensajes enviados por el usuario.
# REQ-11: Permite revisar las respuestas asociadas para contextualizar la conversación.
# REQ-12: Accede al repositorio donde se almacenan los mensajes y respuestas.

class GetConversationService:
    def __init__(self, message_repo: MessageRepositoryPort):
        self.message_repo = message_repo

    def get_conversation(self, user_id: str) -> List[Message]:
        """
        Retorna la lista de mensajes y respuestas asociadas de un usuario.
        """
        conversation = self.message_repo.get_messages_by_user(user_id)
        return conversation
