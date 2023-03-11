import json
import datetime
import boto3
import csv
import tempfile

  
  
  
def poner_datos(event, context):
    nuevo = event['Records'][0]['s3']['object']['key']
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('daticosparcial')
    obj = bucket.Object(nuevo)

    a = obj.find_all('script', {'type': 'application/ld+json'})
    a_lines = str(str(a).splitlines()[1:-1])
    a_lista_casas = [casa for casa in a_lines.split('image')[1:]]
    diccionario_casas = {}
    lista_info = []
    for casa in a_lista_casas:
        diccionario_casas['imagen'] ='https://' + casa.split('jpg')[0].split('https://')[1] + 'jpg'
        diccionario_casas['titulo'] = casa.split('"name": ')[1].split('"description": ')[0]
        diccionario_casas['descripcion'] = casa.split('"description": ')[1].split('",')[0]
        lista_info.append(diccionario_casas)
    #poner la info en un bucket de s3
    s3 = boto3.resource('s3')
    #s3.Bucket('zappa-ej8reqceh').put_object(Key='info3.json', Body=str(lista_info))
    s3.Bucket('daticosparcial').put_object(Key='datos_finales.json', Body=str(diccionario_casas))



    return {
        'statusCode': 200,
        'body': json.dumps('Ya esta 2')
    }
  