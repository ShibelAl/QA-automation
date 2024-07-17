import requests
class APIWrapper:
    def __init__(self):
        self._request = None

    def get_api_request(self):
        return self._request

    def get_request(self, url, body=None):
        return requests.get(url, json=body)