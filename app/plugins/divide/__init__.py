import sys
from app.commands import Command
from calculator.calculation import Calculation
from calculator.operations import divide
from decimal import Decimal

class DivideCommand(Command):
    def __init__(self, history):
        self.history = history
   
    def execute(self, *args):
        if len(args) != 2:
            return "Divide Command requires two arguments."
        try:
            first_input, second_input = Decimal(args[0]), Decimal(args[1])
            if second_input == 0:
                raise ValueError("Cannot divide by zero")
            calc = Calculation(first_input, second_input, divide)

            result = calc.perform()
            self.history.add_record(f"Divide ({first_input}, {second_input})",  result)
            return f"Divide Command result for inputs {first_input}, {second_input} is {result}"

        except ValueError as e:
            return e
