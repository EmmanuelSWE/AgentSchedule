# helper class with methods 
# author : Emmanuel Ashimwe
from abc import ABC, abstractmethod


class Helper:
    @abstractmethod
    def validate(prompt : str):
        try:
            return (int(input(prompt)))
        except ValueError:
            print("Invalid error retry \n going back to previous menu")
            return None