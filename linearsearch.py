arr = [5,44,88,9092,11,90]
def linearSearch(arr,x):
    for i in range(len(arr)):
        if arr [i]==x:
            return i 
    return -1 
x=   int(input("element dal bey: "))
result = linearSearch(arr,x)
if result!=-1:
    print(f"eement hai bhai, kidar ? yaha {result}")
else:
    print("maal nhi hai re baba" )