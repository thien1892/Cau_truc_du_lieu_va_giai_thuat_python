def binary_search(arr, k):
    min, max , mid = 0, len(arr) - 1, 0
    while min <= max :
        mid = (min + max) // 2
        if arr[mid] > k:
            max = mid - 1
        elif arr[mid] < k:
            min = mid + 1
        else:
            return mid
    return -1
