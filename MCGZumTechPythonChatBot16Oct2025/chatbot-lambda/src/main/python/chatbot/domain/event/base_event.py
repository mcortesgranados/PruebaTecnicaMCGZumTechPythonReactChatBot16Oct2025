# 🏢 domain/event/base_event.py

# Este archivo define la clase base para todos los eventos de dominio del chatbot.
# Explicación de requerimientos:
# REQ-05: Permite manejar eventos relacionados con mensajes enviados por el usuario.
# REQ-11: Facilita la contextualización de respuestas al propagar eventos de mensajes.
# REQ-12: Los eventos pueden ser consumidos por adaptadores que interactúan con repositorios.

from datetime import datetime

class BaseEvent:
    """
    Clase base para eventos de dominio.
    Todos los eventos derivados deben incluir al menos la marca de tiempo.
    """

    def __init__(self, occurred_at: datetime = None):
        self.occurred_at = occurred_at or datetime.utcnow()
