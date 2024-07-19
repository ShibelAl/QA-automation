import requests


class APIWrapper:
    def __init__(self):
        self._request = None

    @staticmethod
    def get_request(url, header):
        return requests.get(url, headers=header)
