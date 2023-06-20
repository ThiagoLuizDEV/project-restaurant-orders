from models.ingredient import Ingredient
import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish1 = Dish("lasanha berinjela", 27.00)
    dish2 = Dish("açucar", 17.00)
    other = Dish("", 10.00)

    assert dish1.__hash__() == dish1.__hash__()
    assert dish1.__hash__() != dish2.__hash__()
    assert dish1.__repr__() == "Dish('lasanha berinjela', R$27.00)"
    assert other.name == ''
    assert dish1 == dish1

    dish1.add_ingredient_dependency(Ingredient('queijo mussarela'), 200)
    dish1.add_ingredient_dependency(Ingredient('farinha de trigo'), 200)
    dish1.add_ingredient_dependency(Ingredient('água'), 200)
    dish1.add_ingredient_dependency(Ingredient('berinjela'), 200)
    dish1.add_ingredient_dependency(Ingredient('sal'), 8)
    dish1.add_ingredient_dependency(Ingredient('tomate'), 200)

    assert dish1.get_ingredients() == set([Ingredient('queijo mussarela'),
                                           Ingredient('farinha de trigo'),
                                           Ingredient('água'),
                                           Ingredient('berinjela'),
                                           Ingredient('sal'),
                                           Ingredient('tomate'),
                                           ])
    assert dish1.get_restrictions() != set('')

    with pytest.raises(TypeError):
        Dish("lasanha berinjela", 'R$25.90')   
    with pytest.raises(ValueError):
        Dish("lasanha berinjela", -25.90)