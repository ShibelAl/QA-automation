from infra.config_provider import ConfigProvider


class Bids:
    def __init__(self, request):
        self._request = request
        self._config = ConfigProvider().load_config_json()

    def post_retrieve_authchallenge(self):
        url = f"{self._config['base_url']}/{self._config['retrieve_authchallenge_endpoint']}"
        return self._request.post_request(url, self._config['retrieve_authchallenge_payload'],
                                          self._config['retrieve_authchallenge_headers'])

    # def post_retrieve_accesstoken(self):
    #     url = f"{self._config['base_url']}/{self._config['retrieve_accesstoken_endpoint']}"
    #     auth_key = self.post_retrieve_authchallenge().json()['message']
    #     return self._request.post_request(url, self._config['retrieve_accesstoken_payload'],
    #                                       self._config['retrieve_accesstoken_headers'], auth_key)

    def get_retrieve_executable_bids(self):
        url = f"{self._config['base_url']}/{self._config['retrieve_executable_bids_endpoint']}"
        return self._request.get_request(url, self._config['header_1'])

    def get_retrieve_user_bids(self):
        url = f"{self._config['base_url']}/{self._config['retrieve_user_bids_endpoint']}"
        return self._request.get_request(url, self._config['header_1'], self._config['retrieve_user_bids_querystring'])

    def post_bids_cancel(self):
        url = f"{self._config['base_url']}/{self._config['bids_cancel_endpoint']}"
        return self._request.post_request(url, self._config['bids_cancel_headers'], self._config['bids_cancel_payload'])
