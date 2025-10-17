# 🧩 application/port/input/chatbot_usecase.py

from chatbot.application.port.output.message_repository_port import MessageRepositoryPort
from chatbot.application.port.output.event_publisher_port import EventPublisherPort
from chatbot.domain.model.message import Message, Response

# Explicación de requerimientos:
# REQ-05: Permite procesar y registrar mensajes del usuario.
# REQ-11: Facilita la contextualización, asociando mensajes a respuestas.
# REQ-12: Se conecta con el repositorio para persistencia y recuperación.

class ChatbotUseCase:
    """
    Caso de uso principal del chatbot, coordinando envío y recuperación de mensajes.
    """

    def __init__(self, message_repository: MessageRepositoryPort, event_publisher: EventPublisherPort):
        self.message_repository = message_repository
        self.event_publisher = event_publisher

    def send_message(self, user_id: str, content: str) -> Response:
        """
        Procesa un mensaje enviado por el usuario.

        :param user_id: Identificador del usuario
        :param content: Contenido del mensaje
        :return: Respuesta generada para el mensaje
        """
        # Crear entidad de mensaje
        message = Message(user_id=user_id, content=content)

        # Guardar mensaje en el repositorio
        self.message_repository.save_message(message)

        # Generar respuesta básica (puede ser extendida con lógica de IA)
        response = Response(content=f"Tu mensaje fue recibido: {content}")

        # Asociar respuesta al mensaje
        message.response = response

        # Publicar evento para notificar otros componentes
        self.event_publisher.publish_message_event(message)

        return response
