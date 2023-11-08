
import boto3
import logging
from botocore.exceptions import ClientError
import os

def print_separador():
    print('-' * 50)

def imprimir_mensaje(mensaje):
    print(f'{mensaje:^50}')
    print_separador()

def listar_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    print_separador()
    print('Los siguientes son los buckets existentes:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

def listar_contenido_de_bucket(nombre_bucket):
    s3 = boto3.resource('s3')
    mi_bucket = s3.Bucket(nombre_bucket)
    imprimir_mensaje(f'Archivos en el bucket {nombre_bucket}:')
    for objeto in mi_bucket.objects.all():
        print(f'    {objeto.key}')

def crear_bucket(nombre_bucket, region=None):
    try:
        if region is None:
            s3_cliente = boto3.client('s3')
            s3_cliente.create_bucket(Bucket=nombre_bucket)
        else:
            s3_cliente = boto3.client('s3', region_name=region)
            ubicacion = {'LocationConstraint': region}
            s3_cliente.create_bucket(Bucket=nombre_bucket, CreateBucketConfiguration=ubicacion)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def subir_archivo(nombre_archivo, nombre_bucket, nombre_objeto=None):
    if nombre_objeto is None:
        nombre_objeto = os.path.basename(nombre_archivo)

    s3_cliente = boto3.client('s3')
    try:
        s3_cliente.upload_file(nombre_archivo, nombre_bucket, nombre_objeto)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def eliminar_archivo_de_s3(nombre_bucket, clave_objeto):
    try:
        s3 = boto3.client('s3')
        s3.delete_object(Bucket=nombre_bucket, Key=clave_objeto)
        print(f"Archivo con clave '{clave_objeto}' ha sido eliminado del bucket '{nombre_bucket}'.")
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == "NoSuchKey":
            print(f"El objeto con clave '{clave_objeto}' no existe en el bucket '{nombre_bucket}'.")
        else:
            print(f"Error al eliminar el objeto: {e}")
        return False

def eliminar_bucket(nombre_bucket):
    try:
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(nombre_bucket)
        bucket.objects.all().delete()
        bucket.delete()
        imprimir_mensaje(f"Bucket '{nombre_bucket}' ha sido eliminado.")
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchBucket':
            imprimir_mensaje(f"El bucket '{nombre_bucket}' no existe.")
        else:
            imprimir_mensaje(f"Error al eliminar el bucket: {e}")
        return False


nombre_bucket = 'test-boto3-demo-start'
clave_objeto = 'test.txt'
region = 'us-west-2'
ruta_archivos = '/home/ec2-user/environment/awsRestart/boto3'
archivo1 = '/demo.txt'
archivo2 = '/botoTest.py'

listar_buckets()

imprimir_mensaje(f'Crear bucket: {nombre_bucket}')

if crear_bucket(nombre_bucket, region):
    imprimir_mensaje(f'Bucket: {nombre_bucket} ha sido creado exitosamente.')

imprimir_mensaje('Listar buckets')
listar_buckets()

imprimir_mensaje(f'Subir archivo: {archivo1} al bucket: {nombre_bucket}')
if subir_archivo(ruta_archivos + archivo1, nombre_bucket):
    imprimir_mensaje(f'Archivo {archivo1} ha sido subido exitosamente!')

imprimir_mensaje(f'Subir archivo: {archivo2} al bucket: {nombre_bucket}')
if subir_archivo(ruta_archivos + archivo2, nombre_bucket):
    imprimir_mensaje(f'Archivo {archivo2} ha sido subido exitosamente!')

imprimir_mensaje(f'Listar contenido del bucket con nombre: {nombre_bucket}')
listar_contenido_de_bucket(nombre_bucket)

imprimir_mensaje(f'Eliminar el archivo llamado: {clave_objeto} del bucket llamado: {nombre_bucket}')
eliminar_archivo_de_s3(nombre_bucket, clave_objeto)

imprimir_mensaje(f'Eliminar el bucket llamado: {nombre_bucket}')
eliminar_bucket(nombre_bucket)

print("Los siguientes son los buckets existentes:")
listar_buckets()
