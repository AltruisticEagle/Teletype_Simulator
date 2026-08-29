import time
import csv
import hashlib
import sys
import os

logged_in = False
OUTPUT_SPEED = 0.1



class Teletype():
    def __init__(self):
        self.script = None

    def input_to_teletype(self, log_in: int):
        """code 0 to log in, 1 for new script, 2 for run existing script"""
        if log_in == 0:
            new_user = input("Are you a new user? Y/N ")
            if new_user == "Y":
                new_user = True
            else:
                new_user = None
            
            username = input("Username: ").strip()
            password = hashlib.sha256(input("Password: ").strip().encode()).hexdigest()
            return new_user, username, password

        elif log_in == 1:
            self.script = input("New script name: ")
            self.script += ".txt"
            return None

        elif log_in == 2:
            self.script = input("Name of the script you want to run: ")
            return self.script
        

    def output_from_teletype(self, message):
        for character in message:
            print(character, end="")
            time.sleep(OUTPUT_SPEED)
        print("\n")


    def help(self):
        ...

    def new_program(self):
        """creates a new text program for BASIC code that you write code in"""
        with open(f"user_scripts/{self.script}", "w") as file:
            file.write("New script!\n")

    def load_program(self):
        """loads a written program for the compiler"""
        ...



class BASIC_Interpreter():
    def __init__(self, script_name):
        self.script = read_csv(script_name)

    def interpret(self):
        ...
        



class Computer:
    def __init__(self):
        pass

    def log_in(self, username, password):
        
        rows = read_csv("user_info.csv")
        for row in rows:
            if username == row["username"] and password == row["password"]:
                return True

        return False

    def create_new_user(self, username, password):        
        with open("user_info.csv", "a", newline="") as file:
            fieldnames = ["username", "password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            row = {"username": username, "password": password}
            writer.writerow(row)

    def list_method(self):
        ...

    def print_method(self):
        ...

    def let_method(self, data):
        ...
        #assigns a value to data

    def goto_method(self, line_number):
        ...  
        #goes from one line to another line, skipping lines in between

    def arithmetic(self):
        ...

    def comparison(self):
        ...

    def if_then_method(self):
        ...

    def input_method(self):
        ...

    def for_loop(self):
        ...

    def next_loop(self):
        ...

    def run_program(self):
        ...
        #runs the program

    def end_method(self):
        ...
        #exits the program

def read_csv(file_name):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
    return rows

def main():
    teletype = Teletype()
    computer = Computer()

    if not os.path.exists("user_info.csv"):
        with open("user_info.csv", "w", newline="") as file:
            fieldnames = ["username", "password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

    running = True
    while running:
        global logged_in
        if not logged_in:
            new_user, username, password = teletype.input_to_teletype(0)
            if new_user: 
                computer.create_new_user(username, password)
                teletype.output_from_teletype("Account Created")
                sys.exit(0)

            logged_in = computer.log_in(username, password)
            if not logged_in:
                teletype.output_from_teletype("Login Error")
                sys.exit(1)
            else:
                teletype.output_from_teletype("Logged In")
                continue

        else:
            try:
                a = int(input("Enter 1 to create a new script, enter 2 to run an existing one: "))
            except ValueError:
                print("Invalid input")
                continue

            script = teletype.input_to_teletype(a)
            if a == 1:
                teletype.new_program()
                print("The program will now exit; you can work on the new script.")
                sys.exit(0)
            elif a == 2:
                interpreter = BASIC_Interpreter(script)
                interpreter.interpret()



if __name__ == "__main__":
    main()
    