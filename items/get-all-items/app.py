import json
import os
import boto3

# import requests
session = boto3.Session()
dynamodb = session.resource("dynamodb")
table_name = os.getenv("SAMPLE_TABLE", "undefined")
table = dynamodb.Table(table_name)

_cold_start = True

def get_all():
    # try:
        # ret = table.update_item(
        #     Key={"id": booking_id},
        #     ConditionExpression="id = :idVal",
        #     UpdateExpression="SET #STATUS = :cancelled",
        #     ExpressionAttributeNames={"#STATUS": "status"},
        #     ExpressionAttributeValues={":idVal": booking_id, ":cancelled": "CANCELLED"},
        #     ReturnValues="UPDATED_NEW",
        # )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "hello world python yanai",
                # "location": ip.text.replace("\n", "")
            }),
        }
    # except ClientError as err:
    #     raise BookingCancellationException(details=err)

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    global _cold_start
    if _cold_start:
        _cold_start = False

    # try:
        ret = get_all()

        return ret
    # except BookingCancellationException as err:
    #     raise BookingCancellationException(details=err)

    
