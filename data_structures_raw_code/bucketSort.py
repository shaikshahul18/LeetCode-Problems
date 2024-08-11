def bucketSort(arr):
    counts = [0,0,0] # assuming our array only contains the numbers 0,1,2 
    # if we have more and also we know what those are and are finite range of numbers
    # then we can create arrays accordingly.
    for elem in arr:
        counts[elem] += 1

    i = 0 
    # we use this "i" to make sure that the nested loop below doesn't overflow and the index is out of range,
    # and we also have to replace the elements in the right index
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr


print(bucketSort([1,2,1,2,2,0,1,0]))