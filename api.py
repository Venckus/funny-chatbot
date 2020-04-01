import requests
import json


class Api(object):

    def __init__(self):
        pass

    def api_post(self, api_url, payload):

        raw_response = requests.post(api_url, data=payload)

        response = json.loads(raw_response.text)

        return response

    def api_get(self, url):

        raw_response = requests.get(url)

        return json.loads(raw_response.text)
