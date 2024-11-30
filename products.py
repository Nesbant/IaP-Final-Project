import random 
from persistence import save_line, read_file

def generate_id():
    return random.choice(range(30000, 80001, 5))

def generate_price(product_type):
    if product_type == "computadora":
        return random.choice(range(500, 1501, 2))
    elif product_type == "celular":
        return random.choice(range(300, 801, 3))
    elif product_type == "accesorio":
        return random.choice(range(51, 301, 2))
    else:
        raise ValueError("El tipo de producto no es valido.")
    
def register_product(description, product_type, igv):
    code = generate_id()
    price = generate_price(product_type)
    line = f"{code}|{description}|{product_type}|{igv}|{price}"
    save_line("data/products.txt", line)
    return line

def get_products():
    return read_file("data/products.txt")