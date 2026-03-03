def optimizedBubbleSort(arr):
    n = len(arr) # length of the array

    for i in range(0, n-1):
        swapped = False # optimization flag

        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swapping happened, array is sorted
        if(swapped == False):
            break

    return arr

arr = list(map(int, input().split()))

print(optimizedBubbleSort(arr))

