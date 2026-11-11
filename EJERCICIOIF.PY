nombre = ""
edad = 0
nacionalidad = ""

nombre = input("ingresa tu nombre: ")
edad = int(inputU("ingresa tu edad:"))
nacionalidad = input("ingresa tu nacionalidad: ")

if edad >= 18:# el if va seguido de la condicion y dos puntos
    print("eres mayor de edad")
else:#el else va seguido de dos puntos para decir que se hace si no se cumple la condicion del if
    print("no eres mayor de edad")

if nacionalidad == "N":
    print("eres de nacionalidad mexicana")
else:
    print("no eres de nacionalidad mexicana")        