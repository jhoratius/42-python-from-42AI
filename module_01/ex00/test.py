#!/usr/bin/env python

import sys
import string

from book import Book
from recipe import Recipe

def tests():
    fraisier = Recipe("fraisier", 3, 85, ['flour', 'sugar', 'strawberries', 'water'], "dessert")
    cheesecake = Recipe("cheesecake", 2, 45, ['flour', 'sugar', 'genoise', 'cheese', 'water'], "dessert")
    pancakes = Recipe("pancakes", 1, 25, ['flour', 'sugar', 'baking powder', 'egg', 'milk', 'butter'], "starter")
    
    livre_desserts = Book("Mes recettes")
    livre_desserts.add_recipe(fraisier)
    livre_desserts.add_recipe(cheesecake)

    # get recipe by name
    livre_desserts.get_recipe_by_name("fraisier")
    print("")
    livre_desserts.get_recipe_by_name("cheesecake")
    print("")
    livre_desserts.get_recipe_by_name("citron meringuee")
    print("")

    # add new recipe to the Book
    livre_desserts.add_recipe(pancakes)

    # get recipes by type
    livre_desserts.get_recipes_by_types("starter")

def main():
    try:
        assert len(sys.argv) > 0, "Wrong number of arguments"
        try:
            tests()
        except Exception as e:
            raise e
    except Exception as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()