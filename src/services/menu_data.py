# Req 3
import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path) as line_file:
            data = list(csv.DictReader(line_file))
            dishes = {}

            for row in data:
                name = row['dish']
                price = float(row['price'])
                ingredient = row['ingredient']
                recipe_amount = int(row['recipe_amount'])

                if name not in dishes:
                    dishes[name] = Dish(name, price)

                dish = dishes[name]
                dish.add_ingredient_dependency(
                    Ingredient(ingredient),
                    recipe_amount
                )
                self.dishes.add(dish)
            