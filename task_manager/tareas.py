import json
import os

TAREAS_FILE = "tareas.json"


def saludo(nombre):
    print(f"Hola, {nombre}")

def guardar_tarea(descripcion):
    tarea = {"descripcion": descripcion}
    
    # Si el archivo ya existe, lo abrimos y leemos las tareas anteriores
    if os.path.exists(TAREAS_FILE):
      with open(TAREAS_FILE, 'r', encoding='utf-8') as f:
        tareas = json.load(f) # cargamos el contenido del archivo (una lista)
    else:
        tareas =[] #si no existe el archivo, arrancamos con una lista vacía
    
    tareas.append(tarea)
    
    # Guardamos TODA la lista de tareas en el archivo (sobrescribe el anterior)
    with open(TAREAS_FILE, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)

    print(f"Tarea guardada: {descripcion}")  # feedback visual

    
    
