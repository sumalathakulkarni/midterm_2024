
import sys
from app.commands import Command
from calculator.calculation import Calculation
from calculator.operations import multiply
from decimal import Decimal

class ClearHistoryCommand(Command):

    def __init__(self, history):
        self.history = history

    def execute(self, *args):
        self.history.clear_history()
