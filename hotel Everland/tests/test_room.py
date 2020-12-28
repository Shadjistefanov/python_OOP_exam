import unittest

from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room('name', 3, 1)

    def test_init(self):
        room = Room('name', 3, 1)
        for atr in ['family_name', 'budget', 'members_count', 'children']:
            self.assertTrue(hasattr(room, atr))

        self.assertEqual('name', room.family_name)
        self.assertEqual(3, room.budget)
        self.assertEqual(1, room.members_count)
        self.assertEqual([], room.children)
        self.assertEqual(0, room.expenses)

    # def test_expenses_negative_amount(self):
    #     with self.assertRaises(ValueError) as ctx:
    #         self.room.expenses = -1
    #     self.assertEqual("Expenses cannot be negative", str(ctx.exception))


if __name__ == '__main__':
    unittest.main()