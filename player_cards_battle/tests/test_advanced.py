import unittest

from project.player.advanced import Advanced


INITIAL_HEALTH = 250


class TestAdvanced(unittest.TestCase):
    def test_empty_name_raises(self):
        with self.assertRaises(ValueError):
            a = Advanced("")

    def test_name_is_set(self):
        a = Advanced("Test")
        self.assertEqual(a.username, "Test")

    def test_health_is_set(self):
        a = Advanced("Test")
        self.assertEqual(a.health, INITIAL_HEALTH)

    def test_set_health_negative_value_raises(self):
        a = Advanced("Test")
        with self.assertRaises(ValueError):
            a.health = -10

    def test_is_dead(self):
        a = Advanced("Test")
        self.assertEqual(a.health, INITIAL_HEALTH)
        self.assertFalse(a.is_dead)
        a.health = 0
        self.assertEqual(a.health, 0)
        self.assertTrue(a.is_dead)

    def test_take_damage_raises_with_negative_value(self):
        a = Advanced("Test")
        self.assertEqual(a.health, INITIAL_HEALTH)
        with self.assertRaises(ValueError):
            a.take_damage(-50)

    def test_take_damage(self):
        a = Advanced("Test")
        self.assertEqual(a.health, INITIAL_HEALTH)
        a.take_damage(50)
        self.assertEqual(a.health, 200)

    def test_take_damage_player_will_be_dead(self):
        a = Advanced("Test")
        self.assertEqual(a.health, INITIAL_HEALTH)
        with self.assertRaises(ValueError):
            a.take_damage(260)

