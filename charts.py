import matplotlib.pyplot as plt

def sales_by_product_chart(sales):
    product_totals = {}
    for sale in sales:
        _, product_code, _, _, _, total = sale.split("|")
        total = float(total)
        if product_code in product_totals:
            product_totals[product_code] += total
        else:
            product_totals[product_code] = total

    products = list(product_totals.keys())
    totals = list(product_totals.values())

    plt.figure(figsize=(10, 6))
    plt.bar(products, totals)
    plt.title("Total Sales by Product")
    plt.xlabel("Product Code")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt
