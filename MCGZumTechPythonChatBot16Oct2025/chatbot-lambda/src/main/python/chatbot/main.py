# 🚀 main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from chatbot.adapter.rest.chatbot_controller import router as chatbot_router
from chatbot.adapter.rest.health_controller import router as health_router
from chatbot.infrastructure.exception_handler import setup_exception_handlers
from chatbot.infrastructure.metrics_collector import MetricsCollector

# Explicación de requerimientos:
# REQ-05: Permite exponer los endpoints REST para enviar mensajes y obtener respuestas.
# REQ-06: La aplicación corre en navegador vía REST, sin instalación adicional.
# REQ-07: Compatible con navegadores modernos gracias a la interfaz web simple.
# REQ-08: El frontend puede cargar un index.html y abrir el chat embebido.
# REQ-09: Métricas de tiempo permiten asegurar que el procesamiento de consultas sea rápido.
# REQ-13: Comunicación con repositorios y servicios vía REST seguro.
# REQ-14, REQ-15: Permite discusión de decisiones de diseño, escalabilidad y arquitectura.

app = FastAPI(title="Chatbot Lambda API", version="1.0.0")

# Permitir CORS para desarrollo y prueba desde navegador
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción restringir a dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar el colector de métricas
metrics = MetricsCollector()

# Setup custom exception handlers
setup_exception_handlers(app)

# Agregar routers
app.include_router(chatbot_router, prefix="/chatbot", tags=["Chatbot"])
app.include_router(health_router, prefix="/health", tags=["Health"])

@app.on_event("startup")
async def startup_event():
    print("🚀 Chatbot API iniciada correctamente")

@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 Chatbot API apagada")

# Endpoint raíz opcional para verificar la carga de la página web
@app.get("/")
async def root():
    return {"message": "Chatbot API está corriendo. Accede al chat en /static/index.html"}

# Middleware simple para medir tiempo de respuesta (REQ-09)
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    import time
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    metrics.log_custom_metric("last_request_duration", process_time)
    return response
