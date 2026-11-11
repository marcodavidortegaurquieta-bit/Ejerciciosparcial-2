name= ""
lastname= ""
age= ""
birthday= ""
email= ""
password = ""
confirmpass= ""
opcion= 0

print("bienvenido al sistema de registro de clientes")
print("---------menu pricipal---------")
print("1, registrar clientes")
print("2. buscar imformacion del cliente")
print("3. borrar imformacion del cliente")
print("4. modificar imformacion del cliente")
print("5. salir")
print("---------------------------------")
opcion = (input("selecciona una opcion"))

match opcion:#aqui iniciar el match, que es una validacion de caso

case 1:
name = input("ingresa tu nombre")
lastName = input("Ingresa tu apellido: ")
age = int(input("Ingresa tu edad: "))
birthday = input("Ingresa tu fecha de nacimiento: ")
email = input("Ingresa tu correo electronico: ")
password = input("Ingresa tu contraseña: ")
confirmPass = input("Confirma tu contraseña: ")

case 2:
print("Nombre:", name, "Edad:", age, "Fecha de nacimiento:", birthday, "Correo electrónico:", email,
"Contraseña:", password)

case 3:
name = ""
lastname = ""
age = 0
birthday = ""
email = ""
password = ""

case 4:
name = input("Ingresa tu nombre: ")
lastName = input("Ingresa tu apellido: ")
age = int(input("Ingresa tu edad: "))
birthday = input("Ingresa tu fecha de nacimiento: ")
email = input("Ingresa tu correo electrónico: ")
password = input("Ingresa tu contraseña: ")

case 5:
    print("¡Hasta luego!")
case _:
    print("opcion no valida")