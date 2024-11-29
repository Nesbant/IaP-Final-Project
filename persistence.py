def save_line(filename, line):
    """Appends a line to a file."""
    with open(filename, "a") as file:
        file.write(line + "\n")

def read_file(filename):
    """Reads all lines from a file."""
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
