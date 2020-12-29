import unittest

from project.battle_field import BattleField
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattlefield(unittest.TestCase):
    def test_fight_attacker_is_dead(self):
        attacker = Advanced("Test1")
        enemy = Advanced("Test2")
        attacker.health = 0

        with self.assertRaises(ValueError):
            BattleField.fight(attacker, enemy)

    def test_fight_enemy_is_dead(self):
        attacker = Advanced("Test1")
        enemy = Advanced("Test2")
        enemy.health = 0

        with self.assertRaises(ValueError):
            BattleField.fight(attacker, enemy)

    def test_players_health_is_increased_if_beginers(self):
        pass

    def test_players_health_is_increased(self):
        attacker = Advanced("Test1")
        enemy = Advanced("Test2")
        card = TrapCard("TrapTest")
        attacker.card_repository.add(card)
        enemy.card_repository.add(card)
        self.assertEqual(attacker.health, 250)
        self.assertEqual(enemy.health, 250)

        BattleField.fight(attacker, enemy)
        self.assertEqual(attacker.health, 135)
        self.assertEqual(enemy.health, 135)
        self.assertFalse(attacker.is_dead)
        self.assertFalse(enemy.is_dead)

    def test_enemy_dies_in_battle(self):
        attacker = Advanced("Test1")
        enemy = Beginner("Test2")
        card = TrapCard("TrapTest")
        card_2 = TrapCard("TrapTest2")
        attacker.card_repository.add(card)
        attacker.card_repository.add(card_2)
        enemy.card_repository.add(card)
        self.assertEqual(attacker.health, 250)
        self.assertEqual(enemy.health, 50)
        enemy.health += 175
        BattleField.fight(attacker, enemy)
        self.assertEqual(attacker.health, 260)
        self.assertEqual(enemy.health, 0)

        self.assertFalse(attacker.is_dead)
        self.assertTrue(enemy.is_dead)



