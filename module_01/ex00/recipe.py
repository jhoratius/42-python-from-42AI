
import sys
import string

class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, recipe_type: str, description: str = ""):
        valid_types = ["starter", "lunch", "dessert"]
        if not name or not name.strip():
            raise ValueError("Recipe name cannot be empty or blank!")
        if cooking_time < 0:
            raise ValueError("Cooking time can't be negative")
        if cooking_lvl < 1 or cooking_lvl > 5:
            raise ValueError("Cooking level should be between 1 and 5")
        if recipe_type not in valid_types:
            raise ValueError(f"Recipe type must be one of: {', '.join(valid_types)}")
        if not ingredients:
            raise ValueError("Ingredients list cannot be empty!")

        self.name = name.strip()
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description.strip()

    def __str__(self):
        """The recipe class is a pattern for recipes"""
        str_name = f"--- {self.name} ---"
        str_c_lvl = f"cooking level: {self.cooking_lvl}"
        str_c_time = f"cooking time : {self.cooking_time}"
        str_ingredients = f"ingredients  : {self.ingredients}"
        str_r_type = f"self type  : {self.recipe_type}"
        str_description = f"description  : {self.description}"
            
        final_str = f"{str_name}\n{str_c_lvl}\n{str_c_time}\n{str_ingredients}\n{str_r_type}\n{str_description}"

        return final_str
