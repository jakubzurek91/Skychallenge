
class IllegalCarError(Exception):
    pass


class Car:
    def __init__(self, pax_count, car_mass, gear_count):
        if pax_count > 5:
            raise IllegalCarError("Too many people in the car")
        if car_mass > 2000:
            raise IllegalCarError("Overweight")
        self.__pax_count = pax_count
        self.__car_mass = car_mass
        self.__gear_count = gear_count
        self.__total_mass = self.car_mass + self.pax_count * 70

    @property
    def gear_count(self):
        return self.__gear_count

    @gear_count.setter
    def gear_count(self, new_gearbox):
        if new_gearbox > 6:
            raise IllegalCarError("number of gear out of range")
        else:
            self.__gear_count = new_gearbox

    @property
    def pax_count(self):
        return self.__pax_count

    @pax_count.setter
    def pax_count(self, new_value):
        if new_value > 5:
            raise IllegalCarError("Too many people in the car")
        else:
            self.__pax_count = new_value
            self.__total_mass = self.__car_mass + self.__pax_count * 70

    @property
    def car_mass(self):
        return self.__car_mass

    @car_mass.setter
    def car_mass(self, new_mass):
        if new_mass > 2000:
            raise IllegalCarError("Overweight")
        else:
            self.__car_mass = new_mass
            self.__total_mass = self.__car_mass + self.__pax_count * 70

    @property
    def total_mass(self):
        return self.__total_mass


if __name__=="__main__":
