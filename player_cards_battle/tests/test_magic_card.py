import unittest

from project.card.magic_card import MagicCard

DAMAGE_POINTS = 5
HEALTH_POINTS = 80


class TestMagicCard(unittest.TestCase):
    def test_empty_name_raises(self):
        with self.assertRaises(ValueError):
            a = MagicCard("")

    def test_name_is_set(self):
        a = MagicCard("Test")
        self.assertEqual(a.name, "Test")

    def test_health_is_set(self):
        a = MagicCard("Test")
        self.assertEqual(a.health_points, HEALTH_POINTS)

    def test_set_health_negative_value_raises(self):
        a = MagicCard("Test")
        with self.assertRaises(ValueError):
            a.health_points = -10

    def test_damage_is_set(self):
        a = MagicCard("Test")
        self.assertEqual(a.damage_points, DAMAGE_POINTS)

    def test_set_damage_negative_value_raises(self):
        a = MagicCard("Test")
        with self.assertRaises(ValueError):
            a.damage_points = -10
