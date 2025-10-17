# 🔌 adapter/λ lambda/lambda_handler.py

from fastapi import FastAPI, Request
from mangum import Mangum
from chatbot.adapter.rest.chatbot_controller import router as chatbot_router
from chatbot.adapter.rest.health_controller import router as health_router

# Explicación de requerimientos:
# REQ-06: Permite ejecutar la aplicación sin instalar componentes adicionales, expuesta vía API.
# REQ-07: Compatible con navegadores al exponer endpoints REST.
# REQ-13: Actúa como el punto de entrada seguro al servicio web REST.

app = FastAPI(title="Chatbot API")

# Incluye routers
app.include_router(chatbot_router, prefix="/chatbot")
app.include_router(health_router, prefix="/health")

# AWS Lambda handler
handler = Mangum(app)
