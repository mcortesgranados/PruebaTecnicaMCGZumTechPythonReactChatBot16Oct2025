import os
from dotenv import load_dotenv
import openai
from chatbot.application.port.output.message_repository_port import MessageRepositoryPort
from chatbot.application.port.output.event_publisher_port import EventPublisherPort
from chatbot.domain.model.message import Message, Response

# Cargar variables de entorno
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class SendMessageService:
    def __init__(self, message_repo: MessageRepositoryPort, event_publisher: EventPublisherPort):
        self.message_repo = message_repo
        self.event_publisher = event_publisher
        

    def send_message(self, user_id: str, content: str) -> Response:
        # Crear mensaje de usuario
        message = Message(user_id=user_id, text=content)
        self.message_repo.save_message(message)

        # Llamada a OpenAI usando la nueva API
        openai_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": content}]
        )

        response_text = openai_response.choices[0].message.content

        # Crear objeto Response usando id del mensaje como referencia
        response = Response(message_id=str(id(message)), text=response_text)

        # Asociar respuesta al mensaje
        message.response = response
        self.message_repo.update_message(message)

        # Publicar evento
        self.event_publisher.publish_event({
            "type": "MessageSent",
            "user_id": user_id,
            "message": content,
            "response": response_text
        })

        return response
