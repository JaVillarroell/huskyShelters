import json
import boto3
import base64
import os


animal_adoption_table= os.environ['HUSKY_SHELTERS_TABLE']
huskyTopicName= os.environ['TOPIC_ARN']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(animal_adoption_table)
sns = boto3.resource('sns')
huskyTopic = sns.Topic(huskyTopicName)


#Llega mensaje a todos los emails del topico
#No cambia el valor adopted del resto de pet_ids
#Otros pet_id no deberian tener email ni adopted
def solicitAdoption(event,context):
    path = event["path"]
    array_path = path.split("/")
    email=event["queryStringParameters"]["email"]
    adopt_id =array_path[-1]
    table.put_item(
                Item = {
                    "PK": adopt_id,
                    "SK": 'info',
                    "Adopted": 'false',
                    "Email": email
                })
    huskyTopic.subscribe(
            TopicArn=huskyTopicName,
            Protocol='email',
            Endpoint= email)
    return {
        'statusCode': 200,
        'body': json.dumps("Created Adoption Request ")
    }

def approveAdoption(event,context):
    path = event["path"]
    array_path = path.split("/")
    adopt_id =array_path[-1]
    adoptionClient = table.get_item(
        Key = {
            "PK": adopt_id,
            "SK": 'info'
        }
   )
    print(adoptionClient['Item'])
    table.put_item(
                Item = {
                    "PK": adopt_id,
                    "SK": 'info',
                    "Adopted": 'true',
                    "Email": adoptionClient['Item']['Email']
                })
   
    message = adoptionClient['Item']['Email'] + " su adopcion fue aceptada"    
    huskyTopic.publish(
                Message=message
            )
    return {
        'statusCode': 200,
        'body': json.dumps("Accepted Adoption Request ")
    }