import argparse
from task_manager.tareas import saludo, guardar_tarea, listado




def main():
    parser = argparse.ArgumentParser(description='Saludador')
    parser.add_argument('--nombre',type=str, help='Tu nombre')
    parser.add_argument('--tarea',type=str, help='Ingresar tarea')
    parser.add_argument('--lista',action='store_true', help='Lista de tareas')
    args = parser.parse_args()


    if args.nombre:
       saludo(args.nombre)
    
    if args.tarea:
       guardar_tarea(args.tarea)

    if args.lista:
      listado()
      







if __name__ == "__main__":
    main()
 