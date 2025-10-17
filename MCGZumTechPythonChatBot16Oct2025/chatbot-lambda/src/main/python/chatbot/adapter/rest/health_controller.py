# 🔌 adapter/🌐 rest/health_controller.py

from fastapi import APIRouter
from datetime import datetime

# Explicación de requerimientos:
# REQ-06: Permite verificar que el backend esté corriendo sin requerir instalación de componentes adicionales.
# REQ-07: Compatible con cualquier navegador moderno.
# REQ-14: Permite discutir decisiones de diseño y monitoreo del servicio.
# REQ-17: Facilita la supervisión del estado de la aplicación para la seguridad y confiabilidad.

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Endpoint de salud del servicio.
    Retorna información básica del estado del backend.
    """
    return {
        "status": "UP",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
