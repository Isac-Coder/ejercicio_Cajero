import time
import random
from ansi_colores import *

def cargar():
    print(f"{VERDE}Cargando", end="")
    for _ in range(3):
        time.sleep(random.uniform(0.5, 1.5))
        print(".", end="", flush=True)