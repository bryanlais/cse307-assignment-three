# CSE 307 Assignment :three:

## Student Information :mortar_board:
- Name: Bryan Lai
- ID: 113789803 
- Professor: Yanhong (Annie) Liu

## Python :snake:: a3main.py
This file was written using Python 3.9 and uses TPG and sys.
It reads a file with expressions separated by new lines and follows the guidelines in the assignment listed down below.

To run this file, type ```py a3main.py <.txt file with correct format>```
One example of running this with one of the test .txt files is ```py a1main.py testfiles/a3input1.txt```
Doing this will lead to the desired output being printed in stdout.

## Project Implementation (AST!) 
:one: If the input program contains a syntax error, your analysis program should print "Parsing Error".

:two: If not, the program should print the definitions and uses of procedure names as they are encountered in the first pass of analysis (in the form of "Definition of procedure p" and "Call of procedure p" for procedure "p"), and print "Analysis Error" if (1) a procedure that is already defined is being defined again, or (2) at the end of the program, a procedure that was called was never defined.

:three: If no error is encountered in analyzing procedure names, your program should print the definitions and uses of variables as they are encountered in the second pass of analysis (in the form of "Definition of variable v", "Use of variable v", "Locals of procedure p: v1, v2, ...", and "Shadowing of global variable v"), and print "Analysis Error" if a variable that is not yet defined is being used.

## Sources Used/Afterword :book:
To complete this assignment, I checked the Official Python Library for help on specific syntax and reviewed information on the slides that Professor Annie had shown us in lecture about the different edge cases (including duplicate paramters in methods, or uncalled methods).
