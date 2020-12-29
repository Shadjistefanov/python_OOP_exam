import unittest

from project.card.magic_card import MagicCard
from project.card.card_repository import CardRepository


class TestPlayerRepository(unittest.TestCase):
    def test_init_player_set_attributes(self):
        r = CardRepository()
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)

    def test_add_player(self):
        r = CardRepository()
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)
        player = MagicCard("Test")
        r.add(player)
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)

    def test_add_existing_player_raises(self):
        r = CardRepository()
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)
        player = MagicCard("Test")
        r.add(player)
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)

        with self.assertRaises(ValueError):
            r.add(player)

        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)

    def test_remove_player(self):
        r = CardRepository()
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)
        player = MagicCard("Test")
        r.add(player)
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)
        r.remove(player.name)
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)

    def test_remove_empty_player_name_raises(self):
        r = CardRepository()
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)
        player = MagicCard("Test")
        r.add(player)
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)

        with self.assertRaises(ValueError):
            r.remove("")

        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)

    def test_find(self):
        r = CardRepository()
        self.assertEqual(len(r.cards), 0)
        self.assertEqual(r.count, 0)
        card = MagicCard("Test")
        r.add(card)
        self.assertEqual(len(r.cards), 1)
        self.assertEqual(r.count, 1)

        founded = r.find("Test")

        self.assertEqual(founded.name, card.name)
        self.assertEqual(founded.damage_points, card.damage_points)
        self.assertEqual(founded.health_points, card.health_points)
        self.assertEqual(founded, card)

