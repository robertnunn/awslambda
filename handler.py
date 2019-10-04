import json

def evenOdd(num):
    if int(num) % 2:
        return "Odd"
    else:
        return "Even"

def hello(event, context):
    your_num = event["queryStringParameters"]["num"]
    try:
        your_num = int(your_num)
    except:
        your_num = 1
        
    body = {
        "message": "check for even or odd",
        "input": your_num,
        "output": evenOdd(your_num)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def goodbye(event, context):
    body = {
        "message": "Goodbye function fired successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response