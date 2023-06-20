from src.models.ingredient import Ingredient # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    valid = Ingredient('sal')
    invalid = Ingredient("açucar")
    others = Ingredient("")

    assert valid.__hash__() == valid.__hash__()
    assert valid.__hash__() != invalid.__hash__()
    assert valid == valid
    assert others.name == ""
    assert valid.__repr__() == "Ingredient('sal')"
    assert invalid.restrictions == set()
