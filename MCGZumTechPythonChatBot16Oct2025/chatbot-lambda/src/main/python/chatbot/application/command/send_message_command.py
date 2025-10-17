# 🧩 application/command/send_message_command.py

# Comando para enviar un mensaje al chatbot
# Explicación de requerimientos:
# REQ-05: Representa la acción de enviar un mensaje por el usuario.
# REQ-11: Permite encapsular el mensaje para su contextualización.
# REQ-12: Facilita el mapeo a la persistencia (repositorio).

class SendMessageCommand:
    """
    Comando que encapsula la información necesaria para enviar un mensaje al chatbot.
    """

    def __init__(self, user_id: str, text: str):
        """
        :param user_id: identificador único del usuario que envía el mensaje
        :param text: contenido del mensaje
        """
        self.user_id = user_id
        self.text = text
