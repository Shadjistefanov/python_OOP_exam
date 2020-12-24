import unittest

from project.spaceship.spaceship import Spaceship


class TestSpaceShip(unittest.TestCase):
    def test_init(self):
        prob = Spaceship('stefan', 10)
        self.assertEqual(prob.name, "stefan")
        self.assertEqual(prob.capacity, 10)
        self.assertEqual(prob.astronauts, [])

    def test_add_astronauts(self):
        prob = Spaceship('stefan', 0)
        with self.assertRaises(ValueError):
            prob.add("Ivan")

        with self.assertRaises(ValueError):
            prob.add('stefan')

        i = Spaceship('stefan', 10)
        i.add('ivan')
        self.assertEqual(i.name, 'stefan')
        self.assertEqual(i.astronauts,['ivan'])

    def test_remove(self):
        prob = Spaceship('stefan', 0)
        with self.assertRaises(ValueError):
            prob.remove('ivan')

    def test_remove_on(self):
        prob = Spaceship('stefan', 7)
        with self.assertRaises(ValueError):
            prob.remove('stefan')

        self.assertEqual(prob.capacity, 7)
        self.assertEqual(prob.name, 'stefan')
        self.assertEqual(prob.astronauts, [])






