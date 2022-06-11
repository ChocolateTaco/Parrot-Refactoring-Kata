from enum import Enum  # Enum is introduced in Python 3.4.


class ParrotType(Enum):  # If it is not available, just remove it.
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3

class Parrot:

    def __init__(self, type_of_parrot, number_of_coconuts, voltage, nailed):
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed
        self._load_factor = 9.0
        self._base_speed = 12.0

    def speed(self):
        if self.get_type() == ParrotType.EUROPEAN:
            return self.get_base_speed()
        if self.get_type() == ParrotType.AFRICAN:
            return max(0, self.get_base_speed() - self.get_load_factor() * self.get_number_of_coconuts())
        if self.get_type() == ParrotType.NORWEGIAN_BLUE:
            if self.get_nailed_status():
                return 0
            else:
                return self.compute_base_speed_for_voltage(self.get_voltage())

        raise ValueError("should be unreachable")

    def compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self.get_base_speed()])

    def get_load_factor(self):
        return self._load_factor

    def get_base_speed(self):
        return self._base_speed

    def get_voltage(self):
        return self._voltage

    def get_number_of_coconuts(self):
        return self._number_of_coconuts

    def get_type(self):
        return self._type

    def get_nailed_status(self):
        return self._nailed