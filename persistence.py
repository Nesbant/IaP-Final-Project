def save_line(filename, line):
    with open(filename, "a") as file:
        file.write(line + "\n")

def read_file(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
