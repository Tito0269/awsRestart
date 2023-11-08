import os
import subprocess

# Solicitar al usuario el nombre del nuevo usuario y su contraseña
nuevo_usuario = input("Ingrese el nombre del nuevo usuario: ")
contrasena = input("Ingrese la contraseña para el nuevo usuario: ")

# Crear el nuevo usuario en el sistema
comando_creacion_usuario = f"sudo useradd -m {nuevo_usuario}"
subprocess.run(comando_creacion_usuario, shell=True)

# Solicitar al usuario la ruta completa del directorio
directorio = input("Ingrese la ruta completa del directorio al que se le asignarán permisos: ")

# Asignar al nuevo usuario permisos de propietario sobre el directorio
comando_asignar_permisos = f"sudo chown {nuevo_usuario}:{nuevo_usuario} {directorio}"
subprocess.run(comando_asignar_permisos, shell=True)

print(f"Usuario '{nuevo_usuario}' creado y permisos asignados con éxito en '{directorio}'.")
