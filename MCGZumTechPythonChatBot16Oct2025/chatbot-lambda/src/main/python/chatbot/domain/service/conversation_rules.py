# 🏢 domain/service/conversation_rules.py

# Este archivo define las reglas de negocio para procesar y contextualizar mensajes del chatbot.
# Explicación de requerimientos:
# REQ-05: Permite procesar mensajes y generar respuestas asociadas.
# REQ-11: Contiene la lógica de contextualización, identificando si el mensaje coincide con posibles consultas.
# REQ-12: Se integra con el repositorio de mensajes/respuestas a través de los puertos definidos.

from typing import List, Optional
from chatbot.domain.model.message import Message, Response

class ConversationRules:
    """
    Clase que aplica las reglas de negocio para determinar la respuesta a un mensaje.
    """

    def __init__(self, known_responses: List[Response]):
        self.known_responses = known_responses

    def get_response_for_message(self, message: Message) -> Optional[Response]:
        """
        Determina la respuesta más adecuada para un mensaje dado.
        Actualmente realiza una búsqueda simple por coincidencia exacta de texto,
        pero puede extenderse a búsqueda fuzzy o uso de IA.
        """
        for response in self.known_responses:
            if response.text.lower() == message.text.lower():
                return response
        
        # Si no hay coincidencia exacta, devuelve None para que la capa superior decida
        return None
