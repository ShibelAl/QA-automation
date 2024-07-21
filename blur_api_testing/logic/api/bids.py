from infra.config_provider import ConfigProvider


class Bids:
    def __init__(self, request):
        self._request = request
        self._config = ConfigProvider().load_config_json()

    def retrieve_authchallenge(self):
        url = f"{self._config['base_url']}/{self._config['retrieve_authchallenge_endpoint']}"
        return self._request.post_request(url, self._config['retrieve_authchallenge_headers'],
                                          self._config['retrieve_authchallenge_payload'])

    # def retrieve_accesstoken(self):
        # here i need a private key to retrieve the accesstoken, and since I don't have one,
        # I picked another api to work on, it's LinkedIn api.

    def get_retrieve_executable_bids(self):
        url = f"{self._config['base_url']}/{self._config['retrieve_executable_bids_endpoint']}"
        return self._request.get_request(url, self._config['header_1'])

    def get_retrieve_user_bids(self):
        url = f"{self._config['base_url']}/{self._config['retrieve_user_bids_endpoint']}"
        return self._request.get_request(url, self._config['header_1'], self._config['retrieve_user_bids_querystring'])
