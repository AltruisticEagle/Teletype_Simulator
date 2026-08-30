import sys, time

OUTPUT_SPEED = 0.1

class Teletype():
    def __init__(self):
        self.script_name = None

    def input_to_teletype(self, log_in: int):
        if log_in == 0:
            try:
                self.output_from_teletype("Enter 1 to create a new script, enter 2 to run an existing one: ")
                a = int(input())
            except ValueError:
                print("Invalid input")
                sys.exit(1)
            return a

        elif log_in == 1:
            self.output_from_teletype("New script name: ")
            self.script_name = input()
            self.script_name += ".txt"
            return self.script_name

        elif log_in == 2:
            self.output_from_teletype("Name of the script you want to run: ")
            self.script_name = input()
            self.script_name += ".txt"
            return self.script_name
        
    def output_from_teletype(self, message: str):
        for character in message:
            print(character, end="", flush=True)
            time.sleep(OUTPUT_SPEED)
        print("\n")

    def help(self):
        with open("commands.txt", "r") as file:
            manual = file.read()
        for line in manual:
            print(line)