def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i - 1
        while(j >= 0 and arr[j] > arr[j+1]):
            tmp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = tmp
            j -= 1
    return arr

 