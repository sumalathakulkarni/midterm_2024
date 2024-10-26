 
import sys
from app.commands import Command
from calculator.calculation import Calculation
from calculator.operations import add
from decimal import Decimal

class AddCommand(Command):
    def __init__(self, history):
        self.history = history

    def execute(self, *args):
        if len(args) != 2:
            return "Add Command requires two arguments."
        try:
            first_input, second_input = Decimal(args[0]), Decimal(args[1])
            calc = Calculation(first_input, second_input,add)
            
            result = calc.perform()
            self.history.add_record(f"Add ({first_input}, {second_input})",  result)
            return f"Add Command result for inputs {first_input}, {second_input} is {result}"

        except ValueError:
            return "Invalid numbers provided."
