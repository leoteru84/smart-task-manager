import argparse
from task_manager.tareas import saludo




def main():
    parser = argparse.ArgumentParser(description='Saludador')
    parser.add_argument('--nombre',type=str, help='Tu nombre')
    args = parser.parse_args()


    saludo(args.nombre)






if __name__ == "__main__":
    main()
 