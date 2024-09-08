import boto3
import json
dynamodb = boto3.resource('dynamodb')
table=dynamodb.Table('customer')
client = boto3.client('sns')
def lambda_handler(event, context):
    data = json.dumps(event)
    a=json.loads(data)
    customerid=a["customerid"]
    things=a["things"]
    requsetquantity=a[things]
    
    response = table.get_item(Key={'customerid': customerid})
    
    checkquantity=response["Item"][things]
    
    if requsetquantity<=checkquantity:
        
        table.update_item(
            Key={'customerid': customerid},
            UpdateExpression='SET {} = :val1'.format(things),
            ExpressionAttributeValues={
                ':val1': requsetquantity}
                )
        if things=='Egg' and requsetquantity<=2 :
            level="Currently you have only "+ str(requsetquantity)+ " eggs left."
            message = client.publish(TargetArn='arn:aws:sns:us-west-2:766100636295:crticallevel', Message=level, Subject='Please by eggs')
        
        
        
    return {"item": requsetquantity, "message": "Succussful"}