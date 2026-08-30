import sys, time

OUTPUT_SPEED = 0
"""A teletype returns about 10 characters per second according to research; the output speed is also hardwired to this in this program."""

class Teletype():
    def __init__(self):
        self.script_name = None

    def input_to_teletype(self, log_in: int):
        if log_in == 0:
            try:
                self.output_from_teletype("Enter 1 to create a new script, 2 to run an existing one, 3 to exit, \"commands\" for command menu: ")
                option = input("\nINPUT > ")
                if option not in ["1", "2", "3", "commands"]:
                    raise ValueError

                if option == "commands":
                    self.commands()
                    print()
                    sys.exit(0)
                option = int(option)

            except ValueError,:
                #Exits if none of the three numeric options are picked
                print("Invalid input")
                sys.exit(1)
            if option == 3:
                sys.exit(0)
            return option

        elif log_in == 1 or log_in == 2: #called by Computer to get a script name
            if log_in == 1:
                self.output_from_teletype("New script name: ") #For new scripts
            else:
                self.output_from_teletype("Name of the script you want to run: ") #For existing scripts
 
            self.script_name = input("\nINPUT > ")
            self.script_name += ".txt" #.txt extension is ADDED TO THE FILE NAME HERE
            return self.script_name
        
        elif log_in == 3: #Called by INPUT in interpreter to get an input from the user
            return input("\nINPUT > ")
        
    def output_from_teletype(self, message: str):
        print("\nOUTPUT > ", end="")
        for character in message:
            print(character, end="", flush=True)
            time.sleep(OUTPUT_SPEED)
            #it outputs character by characteron a line
    
    def commands(self):
        """Displays command menu for help"""
        with open("commands.txt", "r") as file:
            commands = file.read()

        for line in commands.splitlines():
            self.output_from_teletype(line)