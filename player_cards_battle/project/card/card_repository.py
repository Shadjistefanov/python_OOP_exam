class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card):
        card_name = card.name
        names = [c.name for c in self.cards]

        if card_name in names:
            raise ValueError(f"Card {card_name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        card_to_remove = self.find(card)
        self.cards.remove(card_to_remove)
        self.count -= 1

    def find(self, name: str):
        card = [c for c in self.cards if c.name == name][0]
        return card
