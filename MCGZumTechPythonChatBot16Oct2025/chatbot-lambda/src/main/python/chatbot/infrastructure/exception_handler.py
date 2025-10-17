# 🏗️ infrastructure/exception_handler.py

# Explicación de requerimientos:
# REQ-09: Ayuda a manejar errores para que el procesamiento de consultas no supere los 5 segundos.
# REQ-11: Permite retornar mensajes de error contextualizados al usuario.
# REQ-14: Facilita discusión de decisiones de diseño y mejoras durante la entrevista.
# REQ-17: Mejora la seguridad y robustez del backend al manejar excepciones correctamente.

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

# Configurar logger
logger = logging.getLogger("chatbot_infra")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class ExceptionHandler:
    """
    Maneja las excepciones globales de la aplicación
    """

    @staticmethod
    async def handle_exception(request: Request, exc: Exception):
        """
        Captura cualquier excepción y retorna un JSON seguro para el frontend
        """
        logger.error(f"Error en la petición {request.url}: {str(exc)}")
        # REQ-11: Mensaje de error contextualizado
        return JSONResponse(
            status_code=500,
            content={"message": "Ocurrió un error procesando su solicitud. Por favor intente nuevamente."}
        )

# ⚠️ La función debe estar fuera de la clase para poder importarla
def setup_exception_handlers(app: FastAPI):
    """
    Registra manejadores de excepción globales.
    """
    app.add_exception_handler(Exception, ExceptionHandler.handle_exception)