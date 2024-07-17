import unittest
from infra.api.api_wrapper import APIWrapper
from logic.api.shuffle_the_cards import APIShuffleTheCards
from infra.config_provider import ConfigProvider


class TestAPIShuffleTheCards(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider.load_config_json()
        self._api_request = APIWrapper()

    def test_shuffle_the_cards(self):
        deck_of_cards = APIShuffleTheCards(self._api_request)
        shuffled_deck_of_cards = deck_of_cards.shuffle_the_deck()
        shuffled_cards_body = shuffled_deck_of_cards.json()
        print(shuffled_cards_body)
        self.assertTrue(shuffled_cards_body['success'])