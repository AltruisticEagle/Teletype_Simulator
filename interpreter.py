import sys

class BASIC_Interpreter():
    def __init__(self, teletype):
        self.teletype = teletype
        self.script = None
        self.interpreted_script = None

        self.script_variables = dict() 

        self.index = 0

        self.loop_data = dict()

    def interpret(self, script):
        self.script = script
        self.interpreted_script = list()

        for line in self.script.splitlines():
            line = line.split(maxsplit=2)
            if len(line) != 3:
                argument = None
            else:
                argument = line[2].strip()
            interpreted_line = {
                "line_number": int(line[0]),
                "command": line[1].upper(),
                "argument": argument
            }
            self.interpreted_script.append(interpreted_line)

        self.run_program()

    def run_program(self):
        self.index = 0
        while self.index < len(self.interpreted_script):
            current_line = self.interpreted_script[self.index]
            command = current_line["command"]
            argument = current_line["argument"]

            new_index = self.execute(command, argument)
            if new_index is not None:
                self.index = new_index
            else:
                self.index += 1

    def execute(self, command, argument):
        if command == "PRINT":
            self.print_method(argument)
            return None

        elif command == "LET":
            self.let_method(argument)
            return None

        elif command == "GOTO":
            return self.goto_method(argument)

        elif command == "IF":
            action = self.booleans(argument)
            if action:
                self.execute(*action.split())
            return None

        elif command == "INPUT":
            self.input_method(argument)
            return None

        elif command == "FOR":
            self.for_loop(argument)

        elif command == "NEXT":
            new_index = self.next_method(argument)
            if new_index is not None:
                return new_index

        elif command == "END":
            sys.exit(0)

        else:
            print(f"Error on line {self.index}")
            sys.exit(1)

    def print_method(self, argument):
        """prints variables"""
        printed_thing = None
        if argument in self.script_variables:
            printed_thing = self.script_variables[argument]
        else:
            printed_thing = argument
                
        self.teletype.output_from_teletype(str(printed_thing).strip('"'))    

    def let_method(self, argument):
        """assigns a value to data"""
        argument = argument.split("=")
        argument[0] = argument[0].strip()
        argument[1] = argument[1].strip()

        for operator in ["+", "-", "*", "/"]:
            if operator in argument[1]:
                argument[1] = self.evaluate_expression(argument[1])
                break

        self.script_variables[argument[0]] = argument[1]

    def goto_method(self, line_number):
        """goes from one line to another line, skipping lines in between"""
        for index, line in enumerate(self.interpreted_script):
            if line["line_number"] == int(line_number):
                return index

    def evaluate_expression(self, expression):
        """Does basic mathematical calculations; Compares two numbers with operators"""
        expression = expression.split()

        left = expression[0].strip()
        right = expression[2].strip()
        if not left.isnumeric():
            left = int(self.script_variables[left])
        else:
            left = int(left)
        if not right.isnumeric():
            right = int(self.script_variables[right])
        else:
            right = int(right)

        operator = expression[1].strip()
        if operator == "+":
            return left + right
        elif operator == "-":
            return left - right
        elif operator == "*":
            return left * right
        elif operator == "/":
            return left / right
        elif operator == ">":
            return True if left > right else False
        elif operator == ">=":
            return True if left >= right else False
        elif operator == "==":
            return True if left == right else False
        elif operator == "<":
            return True if left < right else False
        elif operator == "<=":
            return True if left <= right else False

    def input_method(self, argument):
        """asks for an input and stores it in a variable"""
        prompt, variable = argument.split(";")
        prompt = prompt.strip()
        variable = variable.strip()

        self.print_method(prompt)
        user_input = self.teletype.input_to_teletype(3)

        self.let_method(f"{variable} = {user_input}")

    def booleans(self, expression):
        """Evaluates boolean expressions"""
        condition, action = expression.split("THEN")
        condition = condition.strip()
        action = action.strip()

        if self.evaluate_expression(condition):
            return action
        else:
            return None

    def for_loop(self, argument):
        """For loop"""
        variable, bound = argument.split("=")
        start, end = bound.split("TO")
        variable = variable.strip()
        start = int(start.strip())
        end = int(end.strip())

        self.script_variables[variable] = start
        self.loop_data[variable] = {"end": end, "start_index": self.index + 1}

    def next_method(self, loop_variable_name):
        """Advances a for loop and see if it should continue"""
        loop_variable_name = loop_variable_name.strip()
        self.script_variables[loop_variable_name] += 1

        loop_variable_value = self.script_variables[loop_variable_name]
        loop_data = self.loop_data[loop_variable_name]

        if loop_variable_value <= loop_data["end"]:
            return loop_data["start_index"]
        
        return None