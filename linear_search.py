def linear_search(list, target):
    for i in range(len(list)):
        if target == list[i]:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found", index )
    else:
        print("Target not found")

numbers = [1,2,3,4,5,6,7,8,9]
result = linear_search(numbers, 12)
verify(result)