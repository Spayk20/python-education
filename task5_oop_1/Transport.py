from Abstruct_Fuel import Gas, Diesel, Electric, Kerosene


class Engine:

    def __init__(self, count: int, power: int, volume: int, *args):
        self.count = count
        self.power = power
        self.volume = volume
        super().__init__(*args)

    @staticmethod
    def stop_engine():
        print("stop")


class Transport:
    condition_type = ["new", "good", "bad"]

    def __init__(self, wheels: int, color: str, condition: str, seats: int, *args):
        self.wheels = wheels
        self.color = color
        self.condition = condition
        self.seats = seats
        super().__init__(*args)

    def __contains__(self, item):
        if item in self.condition_type:
            print("We have this condition")
        self.condition_type.append(item)
        print("I will add this type of condition")


class LightCar(Transport, Engine, Gas):

    def __init__(self, form, *args):
        self.form = form
        super().__init__(*args)


class Bus(Transport, Engine, Diesel):
    def __init__(self, passengers, *args):
        self.passengers = passengers
        super().__init__(*args)


class Truck(Transport, Engine, Electric):
    Transport.wheels = 6

    @classmethod
    def get_wheels(cls):
        return f"Truck has {cls.wheels} wheels"


    # count, power, volume
    light_car_engine = Engine(1, 90, 70)
    truck_engine = Engine(1, 1200, 60)
    print(light_car_engine.count, light_car_engine.power)

    print()
    # wheels, color, condition, seats
    vehicle1 = Transport(4, "red", "new", 5)
    print(vehicle1.color, vehicle1.wheels)
    vehicle2 = Transport(6, "green", "good", 52)
    print(vehicle1 == vehicle2)
