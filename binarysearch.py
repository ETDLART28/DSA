
def binarySearch(arr, x):
    arr.sort()  # Sort the array before searching
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Finds the mid point in integer form
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1  
    
    return -1  # If element is not found, return -1

def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i 
    return -1 

arr = [11,22,33,66,21,59]

# User input for binary search
x = int(input("Bolo bhai konsa element hona: "))  
result = binarySearch(arr, x)

if result != -1:
    print(f"Element hai bhai, kidar? Yaha: {result}")
else:
    print("Maal nhi hai baba")

# User input for linear search
x = int(input("Element dal bey: "))
result = linearSearch(arr, x)

if result != -1:
    print(f"Element hai bhai, kidar? Yaha: {result}")
else:
    print("Maal nhi hai re baba")
