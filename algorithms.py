def bubble_sort(sales):
    n = len(sales)
    for i in range(n):
        for j in range(n - 1):  
            if sales[j][5] > sales[j + 1][5]: 
                temp = sales[j]
                sales[j] = sales[j + 1]
                sales[j + 1] = temp
    return sales



def quicksort(sales):
    if len(sales) <= 1:
        return sales
    pivot = sales[0]
    less = []
    greater = []
    
    for i in range(1, len(sales)):  
        if sales[i][0] <= pivot[0]:  
            less.append(sales[i])
        else:
            greater.append(sales[i])
    
    return quicksort(less) + [pivot] + quicksort(greater)



def binary_search(sales, target):
    low = 0
    high = len(sales) - 1

    while low <= high:
        mid = (low + high) // 2
        if sales[mid][0] == target:  
            return sales[mid]
        elif sales[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return None
