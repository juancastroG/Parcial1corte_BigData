import requests
import random
#beatifoul soup
from bs4 import BeautifulSoup
import boto3
import json
import datetime

def peticion():
    user_agents_list = [
        'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',   
    ]
    r = requests.get('https://homes.mitula.com/searchRE/q-chapinero', headers={'User-Agent': random.choice(user_agents_list)})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup
    
    
    
def app(event, context):
    datos = peticion()
    client = boto3.client('s3')
    actual = datetime.datetime.now()
    nombre = f"{actual.year}-{actual.strftime('%m')}-{actual.strftime('%d')}.txt"
    client.put_object(Body=datos, Bucket='daticosparcial', Key=nombre)
    return {
        'statusCode': 200,
        'body': json.dumps('Se guardan los datos')
    }
  
 
