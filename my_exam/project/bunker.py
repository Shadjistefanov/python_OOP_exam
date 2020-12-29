class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_supply = [o for o in self.supplies if o.__class__.__name__ == 'FoodSupply']
        if len(food_supply) == 0:
            raise IndexError("There are no food supplies left!")
        return food_supply

    @property
    def water(self):
        water_supply = [o for o in self.supplies if o.__class__.__name__ == 'WaterSupply']
        if len(water_supply) == 0:
            raise IndexError("There are no food supplies left!")
        return water_supply

    @property
    def painkillers(self):
        painkiller = [p for p in self.medicine if p.__class__.__name__ == "Painkiller"]
        if len(painkiller) == 0:
            raise IndexError("There are no painkillers left!")

        return painkiller

    @property
    def salves(self):
        salve = [p for p in self.medicine if p.__class__.__name__ == "Salve"]
        if len(salve) == 0:
            raise IndexError("There are no painkillers left!")

        return salve

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if not survivor.needs_healing:
            return
        if medicine_type == "Painkiller":
            medicine = self.painkillers[-1]
        else:
            medicine = self.salves[-1]

        del self.medicine[-1]
        medicine.apply(survivor)
        return f"{survivor.name} healed successfully with {medicine_type}"


    def sustain(self, survivor, sustenance_type):
        if not survivor.needs_sustenance:
            return
        if sustenance_type == "FoodSupply":
            sup = self.food[-1]
        else:
            sup = self.water[-1]

        del self.supplies[-1]
        sup.apply(survivor)
        return f"{survivor.name} sustained successfully with {sustenance_type}"


    def next_day(self):
        for supply in self.survivors:
            supply.needs -= supply.age * 2

        for s in self.survivors:
            self.sustain(s, "FoodSupply")
            self.sustain(s, 'WaterSupply')
