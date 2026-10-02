def binary_search(numbers, target):
    first = 0
    last = len(numbers) - 1
    while first <= last:
        middle = (first + last) // 2
        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            first = middle + 1
        else:
            last = middle - 1

    return None

def verify(index):
    if index is not None:
        print("Target found :" , index )
    else:
        print("Target not found")

numbers = [1,2,3,4,5,6,7,8,9] # must be sorted for binary search
result = binary_search(numbers, 6)
verify(result)

result = binary_search(numbers, 12)
verify(result)
