from teletype import Teletype
from interpreter import BASIC_Interpreter
import sys

class Computer():
    def __init__(self):
        self.teletype = Teletype()
        self.interpreter = BASIC_Interpreter(self.teletype)
        self.script_name = None
        self.script = None

    def configure(self):
        self.teletype.output_from_teletype("Configuring BASIC Interpreter...")

    def get_input(self):
        a = self.teletype.input_to_teletype(0)
        self.script_name = self.teletype.input_to_teletype(a)
        if a == 1:
            self.new_program()
            self.teletype.output_from_teletype("The program will now exit; you can work on the new script.")
            sys.exit(0)
        elif a == 2:
            self.open_program()
            self.interpreter.interpret(self.script)

    def new_program(self):
        with open(f"user_scripts/{self.script_name}", "w") as file:
            file.write("New script!\n")

    def open_program(self):
        try:
            with open(f"user_scripts/{self.script_name}") as file:
                self.script = file.read()
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)
        