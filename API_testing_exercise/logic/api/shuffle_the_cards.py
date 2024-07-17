from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class ShuffleTheCards:
    def __init__(self, request: APIWrapper):
        self._request = request
        self._config = ConfigProvider().load_config_json()

    def shuffle_the_deck(self):
        """
        Requests to shuffle the deck with a specified number of decks.

        :return: Response: The response from the API.
        """
        return self._request.get_request(
            f"{self._config['url']}/new/shuffle/?deck_count={self._config['deck_count']}")
