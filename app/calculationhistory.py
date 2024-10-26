# app/CalculationHistory.py

import pandas as pd
import os

class CalculationHistory:
    def __init__(self, history_file):
        self.history_file = history_file
        self.history = pd.DataFrame(columns=["Expression", "Result"])
        self.load_history()

    def add_record(self, expression, result):
        new_record = pd.DataFrame({"Expression": [expression], "Result": [result]})
        self.history = pd.concat([self.history, new_record], ignore_index=True)
        print(f"Record added: {expression} = {result}")

    def save_history(self):
        self.history.to_csv(self.history_file, index=False)
        print("History saved to file.")

    def load_history(self):
        if os.path.exists(self.history_file):
            self.history = pd.read_csv(self.history_file)
            print("History loaded from file.")
        else:
            print("No history file found.")

    def clear_history(self):
        self.history = pd.DataFrame(columns=["Expression", "Result"])
        print("History cleared.")

    def delete_history_file(self):
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
            print("History file deleted.")
        else:
            print("No history file found to delete.")

    def show_history(self):
        if self.history.empty:
            print("No calculation history available.")
        else:
            print("Calculation History:")
            print(self.history)
