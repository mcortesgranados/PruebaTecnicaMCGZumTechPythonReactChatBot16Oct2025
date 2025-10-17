# 🔌 adapter/💾 persistence/message_repository_adapter.py

from typing import List, Optional
from chatbot.domain.model.message import Message, Response
from chatbot.application.port.output.message_repository_port import MessageRepositoryPort
import json
import os

# Explicación de requerimientos:
# REQ-05: Permite almacenar y recuperar mensajes enviados por el usuario.
# REQ-11: Facilita la contextualización, ya que cada Message puede tener un Response asociado.
# REQ-12: Implementa un repositorio de persistencia usando un archivo JSON local como almacenamiento.

class MessageRepositoryAdapter(MessageRepositoryPort):
    def __init__(self, storage_file: str = "messages.json"):
        self.storage_file = storage_file
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, "w") as f:
                json.dump([], f)

    def save_message(self, message: Message) -> None:
        data = self._load_all()
        data.append({
            "user": message.user,
            "text": message.text,
            "timestamp": message.timestamp,
            "response": message.response.text if message.response else None
        })
        self._save_all(data)

    def get_messages(self) -> List[Message]:
        data = self._load_all()
        messages = []
        for item in data:
            response = Response(text=item["response"]) if item.get("response") else None
            msg = Message(user=item["user"], text=item["text"], timestamp=item["timestamp"], response=response)
            messages.append(msg)
        return messages

    def _load_all(self) -> List[dict]:
        with open(self.storage_file, "r") as f:
            return json.load(f)

    def _save_all(self, data: List[dict]) -> None:
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=2)
