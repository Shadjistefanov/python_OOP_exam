class Survivor:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.needs = 100

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age not valid!")
        self._age = value

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health not valid!")
        if value > 100:
            value = 100
        self._health = value

    @property
    def needs(self):
        return self._needs

    @needs.setter
    def needs(self, value):
        if value < 0:
            raise ValueError("Health not valid!")
        if value > 100:
            value = 100
        self._needs = value
        
    @property
    def needs_sustenance(self):
        if self._needs < 100:
            return True
        return False
    
    @property
    def needs_healing(self):
        if self.health < 100:
            return True
        return False