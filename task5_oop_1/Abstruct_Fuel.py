from abc import ABC, abstractmethod


class Fuel(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Gas(Fuel):
    fuel_type: str = "gas"

    def __init__(self, charge):
        self.charge = charge

    def __str__(self):
        return f"Refilled by {self.fuel_type}"


class Diesel(Fuel):
    fuel_type: str = "diesel"

    def __init__(self, charge):
        self.charge = charge

    def __str__(self):
        return f"Refilled by {self.fuel_type}"


class Electric(Fuel):
    fuel_type: str = "electric"

    def __init__(self, charge):
        self.charge = charge

    def __str__(self):
        return f"Refilled by {self.fuel_type}"


class Kerosene(Fuel):
    fuel_type: str = "kerosene"

    def __init__(self, charge):
        self.charge = charge

    def __str__(self):
        return f"Refilled by {self.fuel_type}"



fuel=Kerosene('fuel for jets')
print(fuel)