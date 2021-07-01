import json
import boto3
import base64
import os
import uuid

animal_adoption_table= os.environ['HUSKY_SHELTERS_TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(animal_adoption_table)
s3 = boto3.client('s3')
bucketName = os.environ['HUSKY_SHELTERS_BUCKET']

def uploadImages(arrayPictures,pet_id,arrayPictureNames):
    a = 0
    # uris=[]
    for picture in arrayPictures:
        name = "images/"+ pet_id+ "/" + arrayPictureNames[a] +".jpg"
        decodeImg = base64.b64decode(picture)
        s3.put_object(Bucket=bucketName,Key=name,Body=decodeImg)
        # location = s3.get_bucket_location(Bucket=bucketName)['LocationConstraint']
        # objectUrl = "https://%s.s3-%s.amazonaws.com/%s" % (bucketName,location, name)
        # uris.append(objectUrl)
        # print("This is the url in s3:",objectUrl)
        a = a + 1
    # return uris
    
def updateInfo(pk,sk,health,age,locationPet,adopted,email):
    response = table.update_item(
        Key={
            'PK':pk,
            'SK':sk
        },
        UpdateExpression="set Age=:a,HealthStatus=:h,LocationPet=:l,Adopted=:d,Email=:e",
        ExpressionAttributeValues={
            ':a': age,
            ':h': health,
            ':l': locationPet,
            ':d': adopted,
            ':e': email
        },
        ReturnValues="UPDATED_NEW"
    )
    return response
def updatePet(event, context):
    message=""
    path = event["path"]
    array_path = path.split("/")
    sk=event["queryStringParameters"]["SK"]
    pet_id =array_path[-1]
    bodyObject = json.loads(event["body"])
    health_status = bodyObject["HealthStatus"]
    adopted = bodyObject["Adopted"]
    email = bodyObject["Email"]
    locationPet = bodyObject["LocationPet"]
    age = bodyObject["Age"]

    if bodyObject["Pictures"]:
        # updateUris = uploadImages(bodyObject["pictures"], pet_id)
        uploadImages(bodyObject["Pictures"], pet_id, bodyObject["PictureNames"])
    updateInfo(pet_id,sk,health_status,age,locationPet,adopted,email)
    return {
        'statusCode': 200,
        'body': json.dumps("updated movie succeded")
    }
def deleteImage(event,context):
    message=""
    path = event["path"]
    array_path = path.split("/")
    imageName=event["queryStringParameters"]["imageName"]
    pet_id =array_path[-1]
    path = "images/" + pet_id +"/" + imageName + ".jpg"
    s3.delete_object(
    Bucket=bucketName,
    Key=path)
    table.delete_item(
        Key={
            'PK': pet_id,
            'SK': 'image_' + imageName + ".jpg"
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps("Image Deleted")
    }