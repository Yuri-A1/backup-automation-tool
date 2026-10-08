# 🗄️ Automated User Backup Tool

Utilidad en Python desarrollada para agilizar tareas preventivas en soporte técnico de nivel 1. Automatiza el empaquetado, compresión y registro histórico de directorios críticos de usuarios antes de mantenimientos o formateos de equipos.

## 📋 Funcionalidades
- **Validación del Sistema de Archivos:** Verifica la integridad y existencia de rutas de origen y destino.
- **Compresión Automatizada:** Empaqueta carpetas completas en archivos `.zip` con marca de tiempo única.
- **Registro Histórico (Logging):** Mantiene una traza con fechas y tamaños de archivo en `historial_respaldos.log`.
- **Portabilidad:** Totalmente compatible con Windows y Linux mediante la biblioteca estándar de Python.

## 🚀 Uso
```bash
python backup.py
