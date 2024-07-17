import unittest
from infra.api.api_wrapper import APIWrapper
from logic.api.shuffle_the_cards import ShuffleTheCards
from logic.api.draw_a_card import DrawACard
from infra.config_provider import ConfigProvider


class TestShuffleTheCards(unittest.TestCase):

    def setUp(self):
        self._config = ConfigProvider.load_config_json()
        self._api_request = APIWrapper()
        self._deck_of_cards = ShuffleTheCards(self._api_request)
        self._shuffled_deck_of_cards = self._deck_of_cards.shuffle_the_deck()
        self._deck_id = self._shuffled_deck_of_cards.json()['deck_id']

    def test_draw_a_card_success_response(self):
        """
        Tests if draw a card or more, will get a success response (for example not 404)
        """
        draw_a_card = DrawACard(self._api_request).draw_a_card(self._deck_id, self._config['default_deck_count'])
        # Act
        draw_a_card_body = draw_a_card.json()
        print(draw_a_card_body)  # print statement just for seeing the json body
        # Assert
        self.assertTrue(draw_a_card_body['success'])

    def test_cards_decrease_equal_to_draw(self):
        """
        Tests if drew for example 1 card, then the remaining will be 51.
        """
        draw_a_card = DrawACard(self._api_request).draw_a_card(self._deck_id, self._config['draw_amount'])
        # Act
        draw_a_card_body = draw_a_card.json()
        print(draw_a_card_body)  # print statement just for seeing the json body
        # Assert
        self.assertEqual(draw_a_card_body['remaining'], self._config['total_cards_in_deck'] - self._config['draw_amount'])
