# 🏢 domain/command/handlers/chatbot_command_handler.py

# Este handler procesa comandos relacionados con el chatbot.
# Explicación de requerimientos:
# REQ-05: Recibe mensajes del usuario y permite manipularlos.
# REQ-11: Facilita la contextualización de la respuesta antes de enviarla al usuario.
# REQ-12: Prepara los mensajes para su persistencia en el repositorio.

from ...model.message import Message, Response
from ...service.conversation_rules import generate_response

class ChatbotCommandHandler:
    """
    Manejador de comandos para procesar mensajes enviados al chatbot.
    """

    def __init__(self, message_repository, event_publisher):
        """
        :param message_repository: instancia que implementa la persistencia de mensajes
        :param event_publisher: instancia que publica eventos relacionados al mensaje
        """
        self.message_repository = message_repository
        self.event_publisher = event_publisher

    def handle_send_message(self, user_id: str, text: str) -> Response:
        """
        Procesa el mensaje del usuario:
        - Crea un Message
        - Genera la respuesta aplicando reglas de conversación
        - Persiste el mensaje y la respuesta
        - Publica un evento de mensaje recibido
        """
        # Crear mensaje
        message = Message(user_id=user_id, text=text)

        # Generar respuesta según reglas de negocio
        response_text = generate_response(text)
        response = Response(text=response_text, message_id=id(message))
        message.response = response

        # Guardar en repositorio
        self.message_repository.save_message(message)

        # Publicar evento
        self.event_publisher.publish_message_received(message)

        return response
