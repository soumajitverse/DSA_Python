def selectionSort(arr):
    n = len(arr) # length of the array
# this will sort the array in ascending order
    for i in range(0, n-1):
        min_index = i # this is the index of the min element
        min_element = arr[i]
        for j in range(i, n):
            if(min_element > arr[j]): 
                min_element = arr[j]
                min_index = j
        arr[i] , arr[min_index] = arr[min_index] , arr[i]

    return arr

arr = list(map(int, input().split()))

print(selectionSort(arr))

