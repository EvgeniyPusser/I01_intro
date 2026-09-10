#This is comment
print('Hello World', end=' ')
print("Hello World", end=" ")
print(list(range(1, 1)))

# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -low - 1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid  # Запоминаем текущий найденный индекс
            high = mid - 1  # И продолжаем искать левее
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if result != -1:
        return result

    return -low - 1

print(binary_search([1, 2, 2, 2, 3, 4, 4, 5], 2))



