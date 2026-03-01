def bubbleSort(arr):
    n = len(arr) # length of the array

    for i in range(0, n-1):
        for j in range(0, n-1-i):
            # it will sort the array in ascending order but if you want to sort it to descending order then write arr[j] < arr[j+1]
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = list(map(int, input().split()))

print(bubbleSort(arr))

