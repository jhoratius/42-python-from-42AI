#!/usr/bin/env python

import sys
import string

cookbook = {
    "Sandwich": {
        'ingredients': [],
        'meal' : '',
        'prep_time' : 0
    },
    "Cake": {
        'ingredients': [],
        'meal' : '',
        'prep_time' : 0
    },
    "Salad": {
        'ingredients': [],
        'meal' : '',
        'prep_time' : 0
    }
}


##### Manage answers from the input
def handle_answers(answer: int):
    if answer == 1:
        # A function that adds a recipe from user input. You will need a name, a list of ingredients, a meal type and a preparation time.
        add_new_recipe()

    if answer == 2:
        # A function that takes a recipe name and delete it.
        while(1):
            recipe_to_delete = input(">>> Enter a recipe to delete: ")
            if recipe_to_delete == 'q':
                break
            if recipe_to_delete in cookbook:
                delete_recipe(recipe_to_delete)
                print(f"You successfully deleted {recipe_to_delete}!")
                break
            else:
                print("Wrong recipe name, try again.")

    if answer == 3:
        # A function that takes a recipe name and prints its details.
        while(1):
            recipe_to_detail = input(">>> Enter a recipe to detail: ")
            if recipe_to_detail == 'q':
                break
            if recipe_to_detail in cookbook:
                print_recipe_details(recipe_to_detail)
                break
            else:
                print("Wrong recipe name, try again.")

    if answer == 4:
        # A function that prints all recipe names.
        print_recipe_names()

    if answer == 5:
        print("Cookbook closed. Goodbye!")
        sys.exit()


##### Print the names of the recipe
def print_recipe_names():
    for name in cookbook:
        print(name)


##### Print the details of a recipe
def print_recipe_details(recipe: str):
    print(f"-- {recipe} recipe --")
    print(f"Ingredients list: {cookbook[recipe]['ingredients']}")
    print(f"To be eaten for {cookbook[recipe]['meal']}.")
    print(f"Takes {cookbook[recipe]['prep_time']} minutes of cooking.")


##### Delete a recipe in the dictionnary
def delete_recipe(recipe: str):
    del cookbook[recipe]


##### Add a new recipe in the dictionnary
def add_new_recipe():
    real_recipe_name = ""
    while(1):
        recipe_name = input(">>> Enter a recipe name: ")
        if recipe_name == 'q':
            return
        if recipe_name in cookbook:
            print("Recipe name already exist, try again.")
            continue
        real_recipe_name = recipe_name
        cookbook[real_recipe_name] = {'ingredients': [], 'meal' : '', 'prep_time' : 0}
        break

    while(1):
        print("Enter 'd' when you're done")
        recipe_ingredient = input(">>> Enter an ingredient to add to the recipe: ")
        if recipe_ingredient == 'd':
            break
        if recipe_ingredient == 'q':
            return
        if recipe_ingredient in cookbook:
            print("Recipe name already exist, try again.")
            continue
        else:
            cookbook[real_recipe_name]["ingredients"].append(recipe_ingredient)
        

    recipe_meal_type = input(">>> Enter the meal type of the recipe: ")
    cookbook[real_recipe_name]["meal"] = recipe_meal_type

    recipe_time_prep = input(">>> Enter the time preparation necessary for the recipe: ")
    cookbook[real_recipe_name]["prep_time"] = recipe_time_prep

    print(f"You successfully created {real_recipe_name}!")


##### Initiate 3 recipes in the cookbook dictionnary
def create_meals():
    cookbook["Sandwich"]["ingredients"].append("ham")
    cookbook["Sandwich"]["ingredients"].append("bread")
    cookbook["Sandwich"]["ingredients"].append("cheese")
    cookbook["Sandwich"]["ingredients"].append("tomatoes")
    cookbook["Sandwich"]["meal"] = "lunch" 
    cookbook["Sandwich"]["prep_time"] = 10
    cookbook["Cake"]["ingredients"].append("flour")
    cookbook["Cake"]["ingredients"].append("sugar")
    cookbook["Cake"]["ingredients"].append("eggs")
    cookbook["Cake"]["meal"] = "dessert"
    cookbook["Cake"]["prep_time"] = 60
    cookbook["Salad"]["ingredients"].append("avocado")
    cookbook["Salad"]["ingredients"].append("arugula")
    cookbook["Salad"]["ingredients"].append("tomatoes")
    cookbook["Salad"]["ingredients"].append("spinach")
    cookbook["Salad"]["meal"] = "lunch"
    cookbook["Salad"]["prep_time"] = 15
    
def main():
    try:
        assert len(sys.argv) > 0, "Wrong number of arguments"
        try:
            input_str = ""
            print("Welcome to the Python Cookbook !")
            create_meals()
            print("List of available options:\n\t1: Add a recipe\n\t2: Delete a recipe\n\t3: Print a recipe\n\t4: Print the cookbook\n\t5: Quit")
            while(1):
                answer = input("\nPlease select an option:\n >> ")
                try:
                    answer = int(answer)
                except ValueError:
                    print("Bad input. Try again.")
                    continue
                handle_answers(answer)
        except AssertionError as e:
            raise e
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()