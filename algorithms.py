def bubble_sort(sales):
    n = len(sales)
    for i in range(n):
        for j in range(0, n - i - 1):
            total_j = float(sales[j].split("|")[5])
            total_next = float(sales[j + 1].split("|")[5])
            if total_j > total_next:
                sales[j], sales[j + 1] = sales[j + 1], sales[j]
    return sales


def quicksort(sales):
    if len(sales) <= 1:
        return sales
    pivot = int(sales[0].split("|")[0])
    less = [x for x in sales[1:] if int(x.split("|")[0]) <= pivot]
    greater = [x for x in sales[1:] if int(x.split("|")[0]) > pivot]
    return quicksort(less) + [sales[0]] + quicksort(greater)


def binary_search(sales, target):
    low, high = 0, len(sales) - 1
    while low <= high:
        mid = (low + high) // 2
        sale_number = int(sales[mid].split("|")[0])
        if sale_number == target:
            return sales[mid]
        elif sale_number < target:
            low = mid + 1
        else:
            high = mid - 1
    return None
