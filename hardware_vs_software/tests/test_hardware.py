import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class HardwareTests(unittest.TestCase):
    def test_init(self):
        hw = Hardware('n', 'Express', 5, 10)
        self.assertEqual(hw.name, 'n')
        self.assertEqual(hw.type, 'Express')
        self.assertEqual(hw.capacity, 5)
        self.assertEqual(hw.memory, 10)
        self.assertListEqual(hw.software_components, [])

    def test_install_not_enough_memory(self):
        hw = Hardware('h', 't', 5, 5)
        sf = Software('s', 't', 3, 20)
        with self.assertRaises(Exception) as e:
            hw.install(sf)
        self.assertEqual('Software cannot be installed', str(e.exception))

    def test_install_not_enough_capacity(self):
        hw = Hardware('h', 't', 5, 5)
        sf = Software('s', 't', 30, 3)
        with self.assertRaises(Exception) as e:
            hw.install(sf)
        self.assertEqual('Software cannot be installed', str(e.exception))

    def test_install_success(self):
        hw = Hardware('h', 't', 5, 5)
        sf = Software('s', 't', 1, 1)
        hw.install(sf)
        self.assertListEqual(hw.software_components, [sf])

    def test_uninstall(self):
        hw = Hardware('h', 't', 5, 5)
        sf = Software('s', 't', 1, 1)
        hw.install(sf)
        self.assertIsNone(hw.uninstall(sf))
        self.assertEqual(hw.software_components, [])


if __name__ == '__main__':
    unittest.main()