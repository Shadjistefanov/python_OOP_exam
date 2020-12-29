class BattleField:
    @staticmethod
    def fight(attacker, enemy):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == "Beginner":
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30

        if enemy.__class__.__name__ == "Beginner":
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30

        attacker.health += sum([c.health_points for c in attacker.card_repository.cards])
        enemy.health += sum([c.health_points for c in enemy.card_repository.cards])

        for card in attacker.card_repository.cards:
            if attacker.is_dead or enemy.is_dead:
                return
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            if attacker.is_dead or enemy.is_dead:
                return
            attacker.take_damage(card.damage_points)


