import unittest

from project.card.trap_card import TrapCard

DAMAGE_POINTS = 120
HEALTH_POINTS = 5


class TestTrapCard(unittest.TestCase):
    def test_empty_name_raises(self):
        with self.assertRaises(ValueError):
            a = TrapCard("")

    def test_name_is_set(self):
        a = TrapCard("Test")
        self.assertEqual(a.name, "Test")

    def test_health_is_set(self):
        a = TrapCard("Test")
        self.assertEqual(a.health_points, HEALTH_POINTS)

    def test_set_health_negative_value_raises(self):
        a = TrapCard("Test")
        with self.assertRaises(ValueError):
            a.health_points = -10

    def test_damage_is_set(self):
        a = TrapCard("Test")
        self.assertEqual(a.damage_points, DAMAGE_POINTS)

    def test_set_damage_negative_value_raises(self):
        a = TrapCard("Test")
        with self.assertRaises(ValueError):
            a.damage_points = -10
