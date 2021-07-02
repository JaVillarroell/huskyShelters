import json
import boto3
import os
from boto3.dynamodb.conditions import Key

pets_table = os.environ['HUSKY_SHELTERS_TABLE']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(pets_table)

def getPetsFull(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    response = table.scan(
        FilterExpression = Key('SK').eq('Dog') | Key('SK').eq('Cat')
    )
    
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
    
def getPetFull(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/user/123"
    array_path = path.split("/") # ["", "user", "123"]
    pet_id = array_path[-1]
    print(pet_id)
    
    response = table.query(
        KeyConditionExpression=Key('PK').eq(pet_id) & Key('SK').begins_with('image')
    )
    
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