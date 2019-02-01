def sumOfElements(npArray):
    sum = 0
    for value in npArray:
        sum = sum + value
    return sum

def countNoOfElements(npArray):
    noOfElements = 0
    for value in npArray:
        noOfElements = noOfElements + 1
    return noOfElements

def mergeSort(npArray):
    if len(npArray) > 1:
        mid = len(npArray) // 2
        L = npArray[:mid]
        R = npArray[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                npArray[k] = L[i]
                i += 1
            else:
                npArray[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            npArray[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            npArray[k] = R[j]
            j += 1
            k += 1