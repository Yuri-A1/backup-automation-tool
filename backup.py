"""
Script de automatización de copias de seguridad para soporte IT.
Copia carpetas críticas, comprime en formato ZIP y registra la operación en un log.
"""

import os
import shutil
import datetime

def crear_respaldo(directorio_origen, directorio_destino):
    # Validar que la carpeta de origen exista
    if not os.path.exists(directorio_origen):
        print(f"[!] Error: La carpeta de origen '{directorio_origen}' no existe.")
        return

    # Crear carpeta de destino si no existe
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)
        print(f"[+] Carpeta de respaldos creada: {directorio_destino}")

    # Generar nombre del archivo con timestamp para no sobreescribir
    marca_tiempo = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo_zip = f"backup_{marca_tiempo}"
    ruta_completa_zip = os.path.join(directorio_destino, nombre_archivo_zip)

    print(f"\nIniciando respaldo de: {directorio_origen}")
    print("Comprimiendo archivos...")

    try:
        # Genera el archivo .zip comprimiendo todo el contenido
        archivo_generado = shutil.make_archive(ruta_completa_zip, 'zip', directorio_origen)
        tamano_mb = os.path.getsize(archivo_generado) / (1024 * 1024)

        print("[OK] Respaldo completado con exito.")
        print(f"Archivo generado: {archivo_generado}")
        print(f"Tamaño: {tamano_mb:.2f} MB")

        # Registrar en archivo de log
        ruta_log = os.path.join(directorio_destino, "historial_respaldos.log")
        with open(ruta_log, "a", encoding="utf-8") as log:
            log.write(f"[{datetime.datetime.now()}] CREADO: {archivo_generado} ({tamano_mb:.2f} MB)\n")

    except Exception as e:
        print(f"[!] Ocurrio un fallo durante el respaldo: {e}")

if __name__ == "__main__":
    # Simulación de prueba: crea carpeta temporal si no existe y respalda
    carpeta_simulada = "datos_usuario_prueba"
    os.makedirs(carpeta_simulada, exist_ok=True)
    with open(os.path.join(carpeta_simulada, "documento_importante.txt"), "w") as f:
        f.write("Informacion sensible del usuario que requiere respaldo antes de formatear.")

    crear_respaldo(directorio_origen=carpeta_simulada, directorio_destino="copias_seguridad")
