# 🏢 domain/model/message.py
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Message:
    user_id: str
    text: str
    timestamp: datetime = datetime.utcnow()
    response: Optional["Response"] = None  # Asociar respuesta más adelante

@dataclass
class Response:
    message_id: str
    text: str
    timestamp: datetime = datetime.utcnow()
