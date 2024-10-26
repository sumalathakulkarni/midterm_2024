
import sys
from app.commands import Command

class ExitCommand(Command):
    def __init__(self, history):
        self.history = history

    def execute(self):
        self.history.save_history()
        print("Exiting...")  # Ensure the message is printed
        sys.exit(0)  # Exit after printing the message