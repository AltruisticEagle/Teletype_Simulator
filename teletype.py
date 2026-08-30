import sys, time

OUTPUT_SPEED = 0

class Teletype():
    def __init__(self):
        self.script_name = None

    def input_to_teletype(self, log_in: int):
        if log_in == 0:
            try:
                self.output_from_teletype("Enter 1 to create a new script, enter 2 to run an existing one, 3 to exit: ")
                a = int(input("INPUT > "))
                print("\n")
            except ValueError:
                print("Invalid input")
                sys.exit(1)
            if a == 3:
                sys.exit(0)
            return a

        elif log_in == 1:
            self.output_from_teletype("New script name: ")
            self.script_name = input("INPUT > ")
            self.script_name += ".txt"
            print("\n")
            return self.script_name

        elif log_in == 2:
            self.output_from_teletype("Name of the script you want to run: ")
            self.script_name = input("INPUT > ")
            self.script_name += ".txt"
            print("\n")
            return self.script_name

        elif log_in == 3:
            return input("INPUT > ")
        
    def output_from_teletype(self, message: str):
        print("OUTPUT > ", end="")
        for character in message:
            print(character, end="", flush=True)
            time.sleep(OUTPUT_SPEED)
        print("\n")

    def help(self):
        with open("commands.txt", "r") as file:
            manual = file.read()
        for line in manual:
            print(line)