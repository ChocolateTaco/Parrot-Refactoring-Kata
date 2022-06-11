from parrot import Parrot, ParrotType
import unittest

class test(unittest.TestCase):
    def test_speedOfEuropeanParrot(self):
        parrot = Parrot(ParrotType.EUROPEAN, 0, 0, False)
        assert parrot.speed() == 12.0


    def test_speedOfAfricanParrot_With_One_Coconut(self):
        parrot = Parrot(ParrotType.AFRICAN, 1, 0, False)
        assert parrot.speed() == 3.0


    def test_speedOfAfricanParrot_With_Two_Coconuts(self):
        parrot = Parrot(ParrotType.AFRICAN, 2, 0, False)
        assert parrot.speed() == 0.0


    def test_speedOfAfricanParrot_With_No_Coconuts(self):
        parrot = Parrot(ParrotType.AFRICAN, 0, 0, False)
        assert parrot.speed() == 12.0


    def test_speedNorwegianBlueParrot_nailed(self):
        parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 1.5, True)
        assert parrot.speed() == 0.0


    def test_speedNorwegianBlueParrot_not_nailed(self):
        parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 1.5, False)
        assert parrot.speed() == 18.0


    def test_speedNorwegianBlueParrot_not_nailed_high_voltage(self):
        parrot = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 4, False)
        assert parrot.speed() == 24.0

if __name__ == '__main__':
    unittest.main()