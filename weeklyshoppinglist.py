
import boto3
import json
dynamodb = boto3.resource('dynamodb')
table=dynamodb.Table('customer')
client = boto3.client('sns')

def lambda_handler(event, context):
    
    response = table.get_item(Key={'customerid': '6777'})
    coffee=str(response["Item"]["Coffee"])
    egg=str(response["Item"]["Egg"])
    milk=str(response["Item"]["Milk"])
    level="Currently you have "+ egg+ " eggs, "+coffee+" kg coffee and "+milk+" ml milk left"
    message = client.publish(TargetArn='arn:aws:sns:us-west-2:766100636295:weeklyshoppinglist', Message=level, Subject='Your Weekly Shooping List')
    return {"item": response, "message": "Succussful"}



