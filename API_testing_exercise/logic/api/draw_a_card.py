from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class DrawACard:
    def __init__(self, request: APIWrapper):
        self._request = request
        self._config = ConfigProvider().load_config_json()

    def draw_a_card(self, deck_id, decks_count):
        return self._request.get_request(
            f"{self._config['base_url']}/{deck_id}/draw/?count={decks_count}"
        )
