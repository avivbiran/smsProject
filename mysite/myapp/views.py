from django.shortcuts import render
import boto3
from pprint import pprint
import uuid
from django.http import HttpResponse

def index(request):
    client = boto3.client('dynamodb')
    unique_id = uuid.uuid4()
    response = client.put_item(
        TableName='avivTable',
        Item={
            'tableRequestId': {
                'S': "{}".format(unique_id),
            }
        }
    )
    print("Insert in to DynamoDB succeeded............")
    pprint(response, sort_dicts=False)

    return HttpResponse(f"item with id {unique_id} added to dynamoDb")