import array as arr
arr1 = arr.array('i',[])

# #Entering number one by one
    # for i in range(l):
    #   n = int(input(f"Enter {i+1}th number: "))
    #   arr1.append(n)
def inputarr():
    while True:
        l = int(input('please enter positive integer for length of array: '))
        if l>0:
            break
    #Entering all numbers in one line
    n = list(map(int,input(f'Enter {l} numbers in same line seperated by space: ').split()))
    if len(n) != l:
        print(f'you have entered {len(n)} numbers only')
        inputarr()
    for i in n:
        arr1.append(i)
    return arr1

#returns poistion of the element if present in array, else returns -1
def search(arr1):
    val = int(input("Enter number to be searched: "))
    try:
        k = arr1.index(val)
    except ValueError as ve:
        k = -1
    return k, val

arr = inputarr()
index, value = search(arr)
print(f'{value} is at position {index} in arr1')
