# Advanced Python Calculator for Software Engineering Graduate Course

## Project Overview
This midterm requires the development of an advanced Python-based calculator application.

## Executing the program
The program can be executed using `python main.py` command <br>
The command will load all past command history and available commands and plugins <br><br>
the `menu` command will display the available command line operations as below: <br>
**Available commands: add, clearhistory, divide, exit, menu, multiply, showhistory, subtract**<br>
All the calculations can be performed using `operation val1 val2` syntax as below: <br>
`add 2 3` <br>
The above command will log the operation details to the command history (also applicaiton logging)<br><br>
It will also display the result as below : <br>
**Record added: Add (2, 3) = 5**<br><br>
If we don't pass enough number of parameters these operations will throw approproate error messages <br>
`add` command will show the below error <br>
**Add Command requires two arguments**.<br><br>
`divide 2 0` will show the below error<br>
**Cannot divide by zero**<br><br>
The `showhistory` and `clearhistory` commands will show the previous command history and clear the command history respectively.<br><br>
## Singleton Pattern for Calculator History
- The CalculationHistory is implemented using singleton pattern to share the functionality across various calculation methods and prevent opening the logging file multiple times
- The Calculator History used Pandas and stores the history as CSV file 
- The extension (.csv) is added to the gitignore to exclude the file from tracking
- The csv file name can be customized via environment variables
- The history can be saved to the file automatically on exit command and it can be viewed / cleared using command line menu options

## Logging
The logging is implemented via custom logging configuration and it uses enviornment variable for the log location
