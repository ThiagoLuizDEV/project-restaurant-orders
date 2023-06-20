# Req 3
import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, newline='') as line_file:
            data = csv.reader(line_file)
        for index in data:
            name = index['dish']
            price = float(index['price'])
            ingredient = index['ingredient']
            recipe_amount = int(index['recipe_amount'])

            dish = Dish(name, price)

            dish.add_ingredient_dependency(
                Ingredient(ingredient),
                recipe_amount)
