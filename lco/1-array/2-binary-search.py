a = [int(x) for x in input().split()]

l = len(a)

v = int(input("Enter value to search: "))

low = 0
high = l - 1
mid = (low + high)//2

iteration = 0

while(True):
    print(iteration, " Mid:", a[mid], " First/Low:",
          a[low], " High/Last:", a[high])
    iteration += 1  
    if(v == a[mid]):
        print("value found at:", mid)
        break
    elif(v > a[mid]):
        low = mid + 1
        mid = (low + high)//2
    elif(v < a[mid]):
        high = mid - 1
        mid = (low + high)//2
    if(low > high):
        print("Value not present")
        break
