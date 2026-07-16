
import sys
import string

class GotCharacter:
    def __init__(self, first_name: str, is_alive: bool = True):

        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self):
        """The recipe class is a pattern for recipes"""
        str_first_name = f"--- {self.first_name} ---"
        str_is_alive = f"cooking level: {self.is_alive}"

        final_str = f"{str_first_name}\n{str_is_alive}"

        return final_str

class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(f"{self.first_name}: {self.house_words}")

    def die(self):
        self.is_alive = False
        print(f"{self.first_name} {self.family_name} just died.")

class Baratheon(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Baratheon"
        self.house_words = "Ours is the Fury"

    def print_house_words(self):
        print(f"{self.first_name}: {self.house_words}")

    def die(self):
        self.is_alive = False
        print(f"{self.first_name} {self.family_name} just died.")