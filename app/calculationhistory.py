# app/CalculationHistory.py

import pandas as pd
import os
import logging

class CalculationHistory:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CalculationHistory, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, history_file):
        if not hasattr(self, 'initialized'):
            self.history_file = history_file
            self.history = pd.DataFrame(columns=["Expression", "Result"])
            self.load_history()
            self.initialized = True

    def add_record(self, expression, result):
        new_record = pd.DataFrame({"Expression": [expression], "Result": [result]})
        self.history = pd.concat([self.history, new_record], ignore_index=True)
        logging.info(f"Record added: {expression} = {result}")

    def save_history(self):
        self.history.to_csv(self.history_file, index=False)
        logging.info("History saved to file.")
        print("History saved to file.")

    def load_history(self):
        if os.path.exists(self.history_file):
            self.history = pd.read_csv(self.history_file)
            logging.info("History loaded from file.")
        else:
            logging.Warning("No history file found.")

    def clear_history(self):
        self.history = pd.DataFrame(columns=["Expression", "Result"])
        logging.info("History cleared.")
        print("History cleared.")

    def delete_history_file(self):
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
            logging.info("History file deleted.")
        else:
            logging.warning("No history file found to delete.")

    def show_history(self):
        if self.history.empty:
            logging.warning("No calculation history available.")
            print("No calculation history available.")
        else:
            print("Calculation History:")
            print(self.history)
