
import sys
from app.commands import Command
from calculator.calculation import Calculation
from calculator.operations import multiply
from decimal import Decimal

class ShowHistoryCommand(Command):

    def __init__(self, history):
        self.history = history

    def execute(self, *args):
        self.history.show_history()
