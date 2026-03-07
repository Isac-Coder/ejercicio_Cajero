import os
import json

# Ruta del archivo JSON (misma carpeta que este archivo)
CARPETA = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_CUENTAS = os.path.join(CARPETA, "cuentas.json")

# Diccionario por defecto si no existe el JSON
CUENTAS_DEFAULT = {
    "isac": {
        "clave": "1234",
        "saldo": 1000,
    },
    "riwi": {
        "clave": "1234",
        "saldo": 1000,
    },
    "abraham": {
        "clave": "2222",
        "saldo": 1000,
    },
    "luis": {
        "clave": "3333",
        "saldo": 1000,
    },
}


def cargar_cuentas():
    """Carga las cuentas desde el archivo JSON. Si no existe, usa el diccionario por defecto y lo guarda."""
    if os.path.exists(ARCHIVO_CUENTAS):
        try:
            with open(ARCHIVO_CUENTAS, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    # No hay archivo o falló la lectura: usar valor por defecto y guardar
    guardar_cuentas(CUENTAS_DEFAULT)
    return CUENTAS_DEFAULT.copy()


def guardar_cuentas(cuentas=None):
    """Guarda el diccionario de cuentas en el archivo JSON. Si no se pasa argumento, guarda CUENTAS del módulo."""
    if cuentas is None:
        cuentas = CUENTAS
    with open(ARCHIVO_CUENTAS, "w", encoding="utf-8") as f:
        json.dump(cuentas, f, indent=2, ensure_ascii=False)


# Diccionario de cuentas (cargado desde JSON o por defecto)
CUENTAS = cargar_cuentas()
