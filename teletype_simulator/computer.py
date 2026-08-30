from teletype_simulator.teletype import Teletype
from teletype_simulator.interpreter import BASIC_Interpreter
import sys

from pathlib import Path

SCRIPT_DIR = Path.home() / "Documents" / "Teletype Simulator" / "user_scripts"
SCRIPT_DIR.mkdir(parents=True, exist_ok=True)

class Computer():
    def __init__(self):
        self.teletype = Teletype()
        """Instance of the Teletype object in Computer"""

        self.interpreter = BASIC_Interpreter(self.teletype)
        """Instance of the interpreter in Computer"""

        self.script_name = None
        """Stores the name of BASIC scripts being ran/created"""

        self.script = None
        """Stores the actual BASIC script once it's loaded by open_program. HAS .txt APPENDED TO IT AT THE END AT INPUT"""

    def configure(self):
        self.teletype.output_from_teletype("Configuring BASIC Interpreter...")
        #just a rizzy little thing I guess

    def get_input(self):
        option = self.teletype.input_to_teletype(0) 
        #Option runs from 1 - 3, 1 being create new program and 2 being opening a program; 3 is exit and is dealt with in Teletype
        #This determines which function of the computer we're going to use

        self.script_name = self.teletype.input_to_teletype(option)
        #This gets the name of the script being created/opened from the user
        
        if option == 1: #creates a new program and exits
            self.new_program()
            self.teletype.output_from_teletype("The program will now exit; you can work on the new script.")
            sys.exit(0)

        elif option == 2: #parses the script into self.script to be interpreted
            self.open_program()
            self.interpreter.interpret(self.script)

    def new_program(self):
        """Opens a new .txt file for the user to write their BASIC scripts in."""
        path = SCRIPT_DIR / self.script_name

        with open(path, "w") as file:
            file.write("New script!\n")

    def open_program(self):
        """Opens an existing .txt file for the interpreter to execute."""
        path = SCRIPT_DIR / self.script_name

        try:
            with open(path) as file:
                self.script = file.read()
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)
        