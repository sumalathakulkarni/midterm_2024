# Advanced Python Calculator for Software Engineering Graduate Course

## Project Overview

This midterm requires the development of an advanced Python-based calculator application.

## Singleton Pattern for Calculator History
- The CalculationHistory is implemented using singleton pattern to share the functionality across various calculation methods and prevent opening the logging file multiple times
- The Calculator History used Pandas and stores the history as CSV file 
- The extension (.csv) is added to the gitignore to exclude the file from tracking
- The csv file name can be customized via environment variables
- The history can be saved to the file automatically on exit command and it can be viewed / cleared using command line menu options

## Logging
The logging is implemented via custom logging configuration and it uses enviornment variable for the log location
