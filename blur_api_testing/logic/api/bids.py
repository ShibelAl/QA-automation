from infra.config_provider import ConfigProvider


class Bids:
    def __init__(self, request):
        self._request = request

    def get_executable_bids(self):
        config = ConfigProvider().load_config_json()
        url = f"{config['base_url']}/{config['executable_bids_endpoint']}"
        return self._request.get_request(url, config['header'])
