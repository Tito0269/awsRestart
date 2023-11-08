import os

# Solicitar al usuario la ruta del directorio a listar
directorio = input("Ingrese la ruta del directorio a listar: ")

if os.path.exists(directorio) and os.path.isdir(directorio):
    contenido = os.listdir(directorio)
    print(f"Contenido del directorio '{directorio}':")
    for item in contenido:
        print(item)
else:
    print(f"El directorio '{directorio}' no existe o no es un directorio válido.")
