import sys
from app.commands import Command
from calculator.calculation import Calculation
from calculator.operations import subtract
from decimal import Decimal

class SubtractCommand(Command):
    def __init__(self, history):
        self.history = history

    def execute(self, *args):
        if len(args) != 2:
            return "Subtract Command requires two arguments."
        try:
            first_input, second_input = Decimal(args[0]), Decimal(args[1])
            calc = Calculation(first_input, second_input, subtract)
       
            result = calc.perform()
            self.history.add_record(f"Subtract ({first_input}, {second_input})",  result)
            return f"Subtract Command result for inputs {first_input}, {second_input} is {result}"

        except ValueError:
            return "Invalid numbers provided."