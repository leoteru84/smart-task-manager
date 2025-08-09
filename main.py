import argparse
from task_manager.tareas import saludo, guardar_tarea




def main():
    parser = argparse.ArgumentParser(description='Saludador')
    parser.add_argument('--nombre',type=str, help='Tu nombre')
    parser.add_argument('--tarea',type=str, help='Ingresar tarea')
    args = parser.parse_args()


    if args.nombre:
       saludo(args.nombre)
    elif args.tarea:
       guardar_tarea(args.tarea)
       listar_tareas()







if __name__ == "__main__":
    main()
 