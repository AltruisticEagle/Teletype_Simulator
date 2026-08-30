import sys

class BASIC_Interpreter():
    def __init__(self, teletype):
        self.teletype = teletype
        self.script = None

    def interpret(self, script):
        self.script = script
        for line in self.script.splitlines():
            if "PRINT" in line:
                self.print_method((line.split(maxsplit=2))[2])

        sys.exit(1)

    def print_method(self, line):
        """prints variables"""  
        self.teletype.output_from_teletype(line.strip('"'))    

    def let_method(self, data):
        """assigns a value to data"""
        ...

    def goto_method(self, line_number):
        """goes from one line to another line, skipping lines in between"""
        ...  

    def arithmetic(self):
        """Does basic mathematical calculations"""
        ...

    def comparison(self):
        """Compares two numbers with operators"""
        ...

    def input_method(self):
        """asks for an input and stores it in a variable"""
        ...

    def for_loop(self):
        """For loop"""
        ...

    def run_program(self):
        """Runs the program"""
        ...

    def end_method(self):
        """Exits the program"""
        ...