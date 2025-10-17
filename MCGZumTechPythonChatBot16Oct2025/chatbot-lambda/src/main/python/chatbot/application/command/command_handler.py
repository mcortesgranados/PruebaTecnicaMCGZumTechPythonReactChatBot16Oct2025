# 🧩 application/command/command_handler.py

from chatbot.domain.command.handlers.chatbot_command_handler import ChatbotCommandHandler
from .send_message_command import SendMessageCommand

# Explicación de requerimientos:
# REQ-05: Procesa comandos de envío de mensajes del usuario.
# REQ-11: Permite la contextualización de la respuesta al pasar el mensaje al handler de dominio.
# REQ-12: Facilita la interacción con el repositorio a través del handler de dominio.

class SendMessageCommandHandler:
    """
    Handler que recibe SendMessageCommand y delega la ejecución al dominio.
    """

    def __init__(self, chatbot_handler: ChatbotCommandHandler):
        self.chatbot_handler = chatbot_handler

    def handle(self, command: SendMessageCommand):
        """
        Procesa el comando enviando el mensaje al chatbot y obteniendo la respuesta.

        :param command: instancia de SendMessageCommand
        :return: respuesta generada por el chatbot
        """
        return self.chatbot_handler.process_message(
            user_id=command.user_id,
            text=command.text
        )
