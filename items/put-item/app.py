import json
import os
import boto3
import decimal

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

# import requests
session = boto3.Session()
dynamodb = session.resource("dynamodb")
table_name = os.environ["SAMPLE_TABLE"]
table = dynamodb.Table(table_name)

_cold_start = True

def put_item_all(varid, name):
    response = table.put_item(
       Item={
            'id': varid,
            'name': name
        }
    )
    
    print("PutItem succeeded:")
    return {"message": "item inserted!!"}

def lambda_handler(event, context):

    global _cold_start
    if _cold_start:
        _cold_start = False

    varid = event.get("id")
    name = event.get("name")
    ret = put_item_all(varid,name)

    return ret