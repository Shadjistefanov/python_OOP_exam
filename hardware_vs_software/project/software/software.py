class Software:
    capacity_consumption: int

    def __init__(self, name: str, type: str, capacity_consumption: int, memory_consumption: int):
        self.name: str = name
        self.type: str = type
        self.capacity_consumption: int = capacity_consumption
        self.memory_consumption: int = memory_consumption
