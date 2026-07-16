
import sys
import string
from datetime import datetime as dt
from recipe import Recipe
from typing import List, Optional

class Book:
    def __init__(self, name: str):
        now = dt.now()

        self.name = name
        self.last_update = now
        self.creation_date = now
        self.recipes_list: dict = {
            "starter": [], "lunch": [], "dessert": []
        }

    def __str__(self):
        """The Book class is a book that manage the recipes"""
        recipes = self.recipes_list
        return final_str

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for category_list in self.recipes_list.values():
            for recipe in category_list:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print(f"{name} recipe not found.")
        return None

    def get_recipes_by_types(self, recipe_type):
        """Gets all recipes names for a given recipe_type """
        matched_recipes = [recipe for recipe in self.recipes_list[recipe_type]]

        for recipe in matched_recipes:
            print(recipe)

    def add_recipe(self, recipe):
        """Adds a recipe to the book and updates last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError("Only Recipe instances can be added.")

        if recipe.recipe_type in self.recipes_list:
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = dt.now()
            print(f"{recipe.name} has been added to the {recipe.recipe_type} list.\n")
        else:
            print(f"Error: '{recipe.recipe_type}' is not a valid category in this book.")

    # formatted_date = now.strftime("%d/%m/%Y")
    # fancy_format = now.strftime("%B %d, %Y - %I:%M %p")
    # Handy Formatting Cheat Sheet:
    # %Y: Year (4 digits, e.g., 2026)
    # %m: Month (2 digits, e.g., 07)
    # %B: Month name (e.g., July)
    # %d: Day of the month (e.g., 16)
    # %H: Hour in 24-hour format (e.g., 14)
    # %I: Hour in 12-hour format (e.g., 02)
    # %M: Minute (e.g., 40)
    # %p: AM/PM indicator