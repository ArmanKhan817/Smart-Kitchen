import json
import boto3
from botocore.vendored import requests

client = boto3.client('sns')

def lambda_handler(event, context):
    
    Milk = requests.get("https://0iqw34xca2.execute-api.us-west-2.amazonaws.com/default/getapi?products=Milk")
    mdata=Milk.json()
    
    Egg = requests.get("https://0iqw34xca2.execute-api.us-west-2.amazonaws.com/default/getapi?products=Egg")
    edata=Egg.json()
    
    Coffee = requests.get("https://0iqw34xca2.execute-api.us-west-2.amazonaws.com/default/getapi?products=Coffee")
    cdata=Coffee.json()
    
    milkcost=mdata["Item"]["price"]
    eggcost=edata["Item"]["price"]
    coffeecost=cdata["Item"]["price"]
            
    milk=my_function(milkcost)
    egg=my_function(eggcost)
    coffee=my_function(coffeecost)
    
    level="Cheapest Milk you can buy from "+ milk+",Egg from "+egg+", coffe from "+coffee
    message = client.publish(TargetArn='arn:aws:sns:us-west-2:766100636295:buyingsuggestion', Message=level, Subject='Buying suggestion')
    return {
        "statusCode": 200,
        "body": level
    }        
    
def my_function(fname):
    
    item=[]
    for j in fname.values():
        item.append(j)
    for i,x in fname.items():
        if x==min(item):
            shop=i
            return(shop)        
            
    


