from hogwarts import get_boggart, get_patronus, get_house, get_potions, validate_name
import unittest
import pytest

class TestHogwarts(unittest.TestCase):
    def test_validate_name(self):
        self.assertEqual(validate_name("Cedric Diggory"), "cedric-diggory")


    def test_get_boggart(self):
        self.assertEqual(get_boggart("cedric", "diggory").strip('""'), "Lord Voldemort")

        with pytest.raises(ValueError):
            assert get_boggart("c3dric", "diggory")


    def test_get_patronus(self):
        self.assertEqual(get_patronus("cedric", "diggory"), "Cedric Diggory has not yet discovered its patronus form")


    def test_get_house(self):
        self.assertEqual(get_house("cedric", "diggory").strip('""'), "Hufflepuff")


    def test_get_potions(self):
        self.assertEqual(get_potions("felix-felicis"), "Makes the drinker lucky")

        with pytest.raises(ValueError):
            assert get_potions("f3lix-f3l1c1s")

if __name__ == "__main__":
    unittest.main()