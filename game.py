class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires):
        """construtor"""
        self.color = color
        self.doors = doors
        self.tires = tires

    def brake(self):
        return "Braking"


class Elcar(object):

    def __init__(self, volt, amper, resist):
        self.volt = volt
        self.amper = amper
        self.resist = resist

    def power(self):
        powers = self.volt * self.amper
        return "Power = %s" % powers





if __name__ == "__main__":
    car = Vehicle("Red", 4, "car")
    print(car.brake())

    elcar = Elcar(220, 10, 13)
    print(elcar.power())
