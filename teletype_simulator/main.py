from teletype_simulator.computer import Computer   

def main():
    computer = Computer()
    computer.configure()
    running = True
    while running:
        computer.get_input()

if __name__ == "__main__":
    main()
    