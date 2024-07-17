import unittest
from infra.api.api_wrapper import APIWrapper
from logic.api.shuffle_the_cards import ShuffleTheCards
from infra.config_provider import ConfigProvider


class TestShuffleTheCards(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider.load_config_json()
        self._api_request = APIWrapper()
        self._deck_of_cards = ShuffleTheCards(self._api_request)

    def test_shuffle_the_cards_success_response(self):
        """
        Tests if shuffled the cards, will get a success response (for example not 404)
        """
        # Arrange
        shuffled_deck_of_cards = self._deck_of_cards.shuffle_the_deck()
        # Act
        shuffled_cards_body = shuffled_deck_of_cards.json()
        print(shuffled_cards_body)  # print statement just for seeing the json body
        # Assert
        self.assertTrue(shuffled_cards_body['success'])

    def test_shuffle_the_cards_works(self):
        """
        Tests if the cards get shuffled after the shuffle function worked,
        asserts if shuffled = True.
        """
        # Arrange
        shuffled_deck_of_cards = self._deck_of_cards.shuffle_the_deck()
        # Act
        shuffled_cards_body = shuffled_deck_of_cards.json()
        print(shuffled_cards_body)  # print statement just for seeing the json body
        # Assert
        self.assertEqual(shuffled_cards_body['shuffled'], True)
