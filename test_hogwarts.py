from hogwarts import get_boggart, get_patronus, get_house, get_potions, validate_name
import pytest

def test_validate_name():
    validate_name("Cedric Diggory") == "cedric-diggory"


def test_get_boggart():
    get_boggart("cedric", "diggory") == "Lord Voldemort"

    with pytest.raises(ValueError):
        get_boggart("c3dric", "diggory")


def test_get_patronus():
    get_patronus("cedric", "diggory") == "Cedric Diggory has not yet discovered its patronus form"


def test_get_house():
    get_house("cedric", "diggory") == ["Ravenclaw"]


def test_get_potions():
    get_potions("felix-felicis") == "Makes the drinker lucky"