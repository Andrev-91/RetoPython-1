nombres = str(input("Ingrese su/s nombre/s: \n"))
if len(nombres) <= 5 and len(nombres) <= 50:
    print("Tu nombre debe tener más de 5 letras pero menos que 50")
else:
    print("Perfecto")


apellidos = str(input("Ingrese su/s apellido/s: \n"))
if len(apellidos) <= 5 and len(nombres) <= 50:
    print("Tu apellido debe tener más de 5 letras pero menos que 50")
else:
    print("Perfecto")

numero_de_telefono = str(input("Ingrese su teléfono: \n"))
if len(numero_de_telefono) > 10:
    print("Tu número de telefono debe ser maximo de 10 digitos")
else:
    print("Perfecto")

correo_electronico = str(input("Ingrese su correo electrónico: \n"))
if len(correo_electronico) <= 5 and len(nombres) <= 50:
    print("Tu correo debe tener más de 5 letras pero menos que 50")

else:
    print("Perfecto")


if len(nombres) <= 5 and len(nombres) <=50:
    print("Los espacios no fueron llenados correctamente")
else:
    print(f"Hola {nombres} {apellidos}, en breve recibiras un correo de confirmación a {correo_electronico}")






