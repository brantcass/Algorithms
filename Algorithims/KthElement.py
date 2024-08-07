def kthElement(arr1, arr2, k):
    if len(arr1) == 0:
        return arr2[k-1]
    if len(arr2) == 0:
        return arr1[k-1]
    if k == 1:
        return min(arr1[0], arr2[0])

    mid1 = len(arr1) // 2
    mid2 = len(arr2) // 2

    if mid1 + mid2 + 1 < k:
        if arr1[mid1] < arr2[mid2]:
            return kthElement(arr1[mid1+1:], arr2, k-mid1-1)
        else:
            return kthElement(arr1, arr2[mid2+1:], k-mid2-1)
    else:
        if arr1[mid1] < arr2[mid2]:
            return kthElement(arr1, arr2[:mid2], k)
        else:
            return kthElement(arr1[:mid1], arr2, k)