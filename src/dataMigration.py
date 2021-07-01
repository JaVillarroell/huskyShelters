import json
import boto3
import os
import urllib.parse

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['HUSKY_SHELTERS_TABLE']
table = dynamodb.Table(table_name)
s3 = boto3.client('s3')

def Migrate(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    link = event['Records'][0]['s3']['object']['key']
    response = s3.get_object(Bucket=bucket,Key=key)
    data_key = key.split("/")
    folder = data_key[0]
    if(folder=='CSV'):
        data = response['Body'].read().decode("utf-8")
        pets = data.split("\n")
        for pet in pets:
            data_pet = pet.split(",")
            folder_name =data_pet[0]
            s3.put_object(Bucket=bucket, Key=('images/'+folder_name+'/'))
            table.put_item(
                Item = {
                    "PK": data_pet[0],
                    "SK": data_pet[1],
                    "HealthStatus": data_pet[2],
                    "Age": data_pet[3],
                    "LocationPet": data_pet[4],
                    "Adopted": data_pet[5],
                    "Email": data_pet[6]
                }
                )
        print("CSV FILE")
    elif(folder=='images' and data_key[2] != ""):
        pet_pk = data_key[1]
        image_name = data_key[2]
        table.put_item(
            Item={
                "PK": pet_pk,
                "SK": "image_"+image_name
            }
        )
        print("IMAGE FILE")
    else:
        print("NOTHING")


