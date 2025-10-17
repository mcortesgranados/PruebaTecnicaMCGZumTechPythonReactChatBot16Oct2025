# 🏗️ infrastructure/metrics_collector.py

# Explicación de requerimientos:
# REQ-09: Permite monitorear tiempos de respuesta del bot para asegurar que las consultas se procesen en menos de 5 segundos.
# REQ-14: Facilita discusión de decisiones de diseño y posibles mejoras en la entrevista.
# REQ-15: Sirve como base para escalar el chatbot y medir su rendimiento en producción.
# REQ-17: Ayuda a identificar problemas de seguridad o rendimiento.

import time
import logging

logger = logging.getLogger("chatbot_metrics")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class MetricsCollector:
    """
    Clase para recolectar métricas de la aplicación
    """

    def __init__(self):
        self.metrics = {}

    def start_timer(self, key: str):
        """
        Inicia un temporizador para medir duración de una operación
        """
        self.metrics[key] = time.time()

    def stop_timer(self, key: str):
        """
        Finaliza el temporizador y registra la duración
        """
        if key in self.metrics:
            duration = time.time() - self.metrics[key]
            logger.info(f"Métrica '{key}' - Duración: {duration:.4f} segundos")
            # Limpiar métrica
            del self.metrics[key]
            return duration
        else:
            logger.warning(f"No se encontró la métrica '{key}' para detener")
            return None

    def log_custom_metric(self, key: str, value):
        """
        Registra una métrica personalizada
        """
        logger.info(f"Métrica personalizada '{key}': {value}")
