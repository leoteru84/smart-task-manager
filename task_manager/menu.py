def menu():

  execute=True
  while execute == True:  
    print("Ingrese la opción deseada")
    print("1- Guardar Tarea")
    print("2- Listar Tarea")
    print("3- Salir")
    opcion = int(input("Opción:"))
        
    if opcion == 1:
       print("dentro de 1")
       
    elif opcion == 2:
       print("dentro de 2")
       
    elif opcion == 3:
       print("dentro de 3")
       
    else:
        execute = False
        print("execute es igual a falso Salir ")

