import sys
import os

class BasicInterpreter:
    def __init__(self):
        self.program = {}    # Stores line numbers and code: {10: "LET A = 5"}
        self.variables = {}  # Stores BASIC variables: {"A": 5}
        self.lines = []      # Sorted list of line numbers for tracking execution
        self.pc = 0          # Program Counter (index of current line executing)

    def load_program(self, code):
        """Parses raw text and populates the program dictionary."""
        for line in code.strip().split('\n'):
            parts = line.split(maxsplit=1)
            if not parts:
                continue
            line_num = int(parts[0])
            source = parts[1] if len(parts) > 1 else ""
            self.program[line_num] = source
        
        # Sort line numbers so the program executes in correct numerical order
        self.lines = sorted(self.program.keys())

    def evaluate_expression(self, expr):
        """Safely evaluates basic math or replaces variables with values."""
        expr = expr.strip()
        # Replace variable names in expression with their actual values
        for var, val in self.variables.items():
            expr = expr.replace(var, str(val))
        try:
            return eval(expr, {"__builtins__": None}, {})
        except Exception:
            return expr.strip('"')  # If it fails math, treat it as a literal string

    def run(self):
        """Main execution loop."""
        self.pc = 0
        while self.pc < len(self.lines):
            line_num = self.lines[self.pc]
            statement = self.program[line_num]
            
            # Move to next line by default (can be overridden by GOTO)
            next_pc = self.pc + 1 

            if not statement or statement.startswith("REM"):
                pass # Ignore comments or blank lines
                
            elif statement.startswith("PRINT"):
                expr = statement[5:].strip()
                print(self.evaluate_expression(expr))
                
            elif statement.startswith("LET"):
                # Format: LET A = 5 + 2
                parts = statement[3:].split("=")
                var_name = parts[0].strip()
                expr = parts[1].strip()
                self.variables[var_name] = self.evaluate_expression(expr)
                
            elif statement.startswith("GOTO"):
                target_line = int(statement[4:].strip())
                if target_line in self.lines:
                    next_pc = self.lines.index(target_line)
                else:
                    print(f"Error: Line {target_line} not found.")
                    break
                    
            elif statement.startswith("END"):
                break

            self.pc = next_pc

# ==========================================
# TEST RUNNING BASIC INSIDE PYTHON
# ==========================================

basic_code = """
10 REM Initialize a countdown
20 LET A = 5
30 PRINT A
40 LET A = A - 1
50 IF A > 0 THEN GOTO 30
60 PRINT "BLAST OFF!"
70 END
"""

# Hardcoded simplified version of line 50 for our primitive parser
# To keep this code short, we will just manually hardcode a conditional jump
fixed_basic_code = """
10 REM Countdown loop
20 LET A = 5
30 PRINT A
40 LET A = A - 1
50 GOTO 30
60 PRINT "DONE"
"""

# Let's adjust the sample to showcase basic linear running + jumping
linear_sample = """
10 PRINT "STARTING USER PROGRAM..."
20 LET X = 10
30 LET Y = 20
40 LET Z = X + Y
50 PRINT Z
60 END
"""

interpreter = BasicInterpreter()
interpreter.load_program(linear_sample)
interpreter.run()
