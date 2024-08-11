def quickSort(arr, start, end):
    if end - start + 1 <= 1:
        return arr
    # The above returns an array if it has only 1 element or no element at all.
    # now we set the pivot, it is usually set as the last element
    pivot = arr[end]
    # we also set the starting pointer, this will be used to swap the elements during the iteration
    # which are less than the pivot element
    leftPointer = start
    for index in range(start,end):
        if arr[index] <= pivot:
            temp = arr[index]
            arr[index] = arr[leftPointer]
            arr[leftPointer] = temp
            leftPointer += 1
        # In the above we are just trying to swap the elements which are less than the pivot element
        # to the left hand side and elements greater than the pivot on the right hand side


    # after we have moved the elements, we want to bring the pivot element in betweeen the left and right side elements
    arr[end] = arr[leftPointer]
    arr[leftPointer] = pivot
    # Now that the pivot is in the right place, we will now sort the left hand side elements and the right hand side elements
    # using RECURSION
    quickSort(arr, start, leftPointer - 1)
    quickSort(arr, leftPointer + 1, end)

    return arr

print(quickSort([6,2,4,1,3],0,4))