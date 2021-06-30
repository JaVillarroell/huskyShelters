import json
import boto3
import os

pets_table = os.environ['HUSKY_SHELTERS_TABLE']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(pets_table)

def getPets(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    response = table.scan()
    
    items = response['Items']
    print(items)
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin" : "*", # Required for CORS support to work
            "Access-Control-Allow-Credentials" : True # Required for cookies, authorization headers with HTTPS 
         },
        'body': json.dumps(items)
    }