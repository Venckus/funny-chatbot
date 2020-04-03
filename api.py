import requests
import json


def build_url(args, city=None):
    'build request url'

    if city != None:
        return f"{args['url']}{city}{args['end']}"


def api_get(url):

    raw_response = requests.get(url)

    if raw_response.status_code != 200:

        return False

    else:
        return json.loads(raw_response.text)


def validate(response):
    'check if api request not failed'

    return response if response['message'] == "SUCCESS" else False
