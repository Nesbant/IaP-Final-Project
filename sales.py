from persistence import save_line, read_file

def generate_sale_number(last_sale=None):
    return last_sale + 1 if last_sale else 100

def calculate_sale_total(price, quantity, igv):
    igv_rate = 0 if igv == "SI" else 0.18
    price_with_igv = round(price * (1 + igv_rate), 2)
    return round(price_with_igv * quantity, 2)

def register_sale(product_code, description, quantity, price, igv_benefit, last_sale=None):
    """Registers a new sale."""
    sale_number = generate_sale_number(last_sale)
    total = calculate_sale_total(price, quantity, igv_benefit)
    line = f"{sale_number}|{product_code}|{description}|{quantity}|{price}|{total}"
    save_line("data/sales.txt", line)
    return line

def get_sales():
    return read_file("data/sales.txt")

def modify_sale_quantity(sale_number, new_quantity):
    sales = read_file("data/sales.txt")
    updated_sales = []
    found = False

    for sale in sales:
        fields = sale.split("|")
        if int(fields[0]) == sale_number:
            found = True
            price = float(fields[4])
            igv_benefit = fields[5]
            total = round(price * new_quantity, 2)
            updated_sale = f"{fields[0]}|{fields[1]}|{fields[2]}|{new_quantity}|{price}|{total}"
            updated_sales.append(updated_sale)
        else:
            updated_sales.append(sale)

    if found:
        with open("data/sales.txt", "w") as file:
            for updated_sale in updated_sales:
                file.write(updated_sale + "\n")
        return True
    else:
        return False

def get_highest_sale():
    sales = read_file("data/sales.txt")
    if not sales:
        return None
    highest_sale = max(sales, key=lambda sale: float(sale.split("|")[5]))
    return highest_sale
