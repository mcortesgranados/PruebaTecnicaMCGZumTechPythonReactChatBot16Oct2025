# 🧩 application/query/get_conversation_query.py

from chatbot.application.port.output.message_repository_port import MessageRepositoryPort

# Explicación de requerimientos:
# REQ-05: Permite obtener los mensajes enviados por el usuario.
# REQ-11: Facilita la contextualización de la conversación al recuperar los mensajes anteriores.
# REQ-12: Interactúa con el repositorio para persistencia y recuperación de datos.

class GetConversationQuery:
    """
    Query para obtener la conversación completa de un usuario.
    """

    def __init__(self, message_repository: MessageRepositoryPort):
        self.message_repository = message_repository

    def execute(self, user_id: str):
        """
        Retorna todos los mensajes y respuestas asociados a un usuario.

        :param user_id: Identificador único del usuario
        :return: Lista de mensajes y respuestas
        """
        return self.message_repository.get_messages_by_user(user_id)
