# 💉 config/app_config.py

import os

# Explicación de requerimientos:
# REQ-12: Configura accesos a repositorios y otros recursos persistentes.
# REQ-13: Permite centralizar configuración de servicios web y seguridad.
# REQ-15: Facilita escalabilidad al permitir cambiar endpoints y claves sin modificar código.

class AppConfig:
    """
    Clase para centralizar la configuración de la aplicación
    """

    # Configuración de OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    # Configuración de SQS
    SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL", "https://sqs.us-east-1.amazonaws.com/123456789012/ChatbotQueue")

    # Configuración SNS
    SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN", "arn:aws:sns:us-east-1:123456789012:ChatbotTopic")

    # Configuración de la base de datos (SQLite como ejemplo)
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///chatbot.db")

    # Tiempo de espera de respuestas del backend
    RESPONSE_TIMEOUT = int(os.getenv("RESPONSE_TIMEOUT", "5"))  # REQ-09

    # Otros parámetros generales
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

    @staticmethod
    def print_config():
        print(f"OpenAI Key: {AppConfig.OPENAI_API_KEY}")
        print(f"SQS Queue URL: {AppConfig.SQS_QUEUE_URL}")
        print(f"SNS Topic ARN: {AppConfig.SNS_TOPIC_ARN}")
        print(f"Database URL: {AppConfig.DATABASE_URL}")
        print(f"Response timeout: {AppConfig.RESPONSE_TIMEOUT}s")
        print(f"Debug mode: {AppConfig.DEBUG}")
