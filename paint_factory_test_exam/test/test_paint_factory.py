import unittest

from project.factory.paint_factory import PaintFactory


class TestFactory(unittest.TestCase):
    def test_structure(self):
        t = PaintFactory("Test", 200)
        self.assertEqual("Test", t.name)
        self.assertEqual(200, t.capacity)
        self.assertEqual({}, t.ingredients)
        self.assertEqual(len(t.valid_ingredients), 5)

    def test_add_ingredient(self):
        t = PaintFactory("Test", 200)
        self.assertEqual({}, t.ingredients)
        self.assertEqual("Test", t.name)
        self.assertEqual(200, t.capacity)
        t.add_ingredient("blue", 50)
        self.assertEqual({'blue': 50}, t.ingredients)
        self.assertEqual(1, len(t.ingredients))


    def test_add_raise_error(self):
        t = PaintFactory("Test", 200)
        self.assertEqual("Test", t.name)
        self.assertEqual(200, t.capacity)
        self.assertTrue(t.capacity, 200)
        with self.assertRaises(ValueError):
            t.add_ingredient("blue", 250)

    def test_wrong_name_raises(self):
        t = PaintFactory("Test", 200)
        self.assertTrue(t.capacity, 200)
        self.assertEqual("Test", t.name)
        self.assertEqual(200, t.capacity)
        with self.assertRaises(TypeError):
            t.add_ingredient("pink", 50)

    def test_remove_ingredient(self):
        t = PaintFactory("Test", 200)
        self.assertTrue(t.capacity, 200)
        self.assertEqual("Test", t.name)
        self.assertEqual(200, t.capacity)
        t.add_ingredient("blue", 50)
        self.assertEqual({'blue': 50}, t.ingredients)
        self.assertEqual(1, len(t.ingredients))
        t.remove_ingredient("blue", 20)
        self.assertEqual({'blue': 30}, t.ingredients)
        self.assertEqual(1, len(t.ingredients))

    def test_remove_ingredient_raises(self):
        t = PaintFactory("Test", 200)
        self.assertTrue(t.capacity, 200)
        self.assertEqual("Test", t.name)
        self.assertEqual(200, t.capacity)
        t.add_ingredient("blue", 50)
        self.assertEqual({'blue': 50}, t.ingredients)
        self.assertEqual(1, len(t.ingredients))
        with self.assertRaises(KeyError):
            t.remove_ingredient("pink", 20)


    def test_ingredient_raises_value_error(self):
        t = PaintFactory("Test", 200)
        self.assertTrue(t.capacity, 200)
        self.assertEqual("Test", t.name)
        self.assertEqual(200, t.capacity)
        t.add_ingredient("blue", 50)
        self.assertEqual({'blue': 50}, t.ingredients)
        self.assertEqual(1, len(t.ingredients))
        with self.assertRaises(ValueError):
            t.remove_ingredient("blue", 150)

    def test_property_ingredients_products(self):
        t = PaintFactory("Test", 200)
        self.assertTrue(t.capacity, 200)
        self.assertEqual("Test", t.name)
        self.assertEqual(200, t.capacity)
        t.add_ingredient("blue", 50)
        self.assertEqual(1, len(t.products))
        self.assertEqual({'blue': 50}, t.products)


