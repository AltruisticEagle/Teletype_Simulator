class BASIC_Interpreter():
    def __init__(self, teletype):
        self.teletype = teletype
        self.script = None
        self.interpreted_script = None

        self.script_variables = dict()

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

        index = 0
        while True:
            current_line = self.interpreted_script[index]
            command = current_line["command"]
            argument = current_line["argument"]

            if command == "PRINT":
                index += 1
                self.print_method(argument)

            elif command == "LET":
                index += 1
                self.let_method(argument)

            elif command == "GOTO":
                index = self.goto_method(argument)

            elif command == "END":
                break

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
        """Does basic mathematical calculations"""
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
        

    def comparison(self):
        """Compares two numbers with operators"""
        ...

    def input_method(self):
        """asks for an input and stores it in a variable"""
        ...

    def for_loop(self):
        """For loop"""
        ...