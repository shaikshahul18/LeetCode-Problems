def mergeSort(arr, start, end):
    if (end-start + 1) <= 1:
        return arr
    mid = (start + end) / 2
    mergeSort(arr,start, mid)
    mergeSort(arr,mid, end)
    merge(arr, start, mid ,end)
    return arr

def merge(arr,start,mid,end):
    L = arr[start:mid+1]
    R = arr[mid+1:end+1]
    i = 0
    j = 0
    k = start
    while (i < len(L) and j < len(R)):
        if L[i] <= R[i]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[i]
            j += 1
        k += 1
    
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1