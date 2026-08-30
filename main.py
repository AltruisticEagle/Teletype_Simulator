from computer import Computer

commands = [
    "PRINT",
    "LET",
    "GOTO",
    "INPUT",
    "FOR",
    "NEXT",
    "RUN",
    "END"
]        

def main():
    computer = Computer()
    computer.configure()
    running = True
    while running:
        computer.get_input()

if __name__ == "__main__":
    main()
    