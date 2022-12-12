def binary_search(arr, k):
    """Binary search

    Parameters
    ----------
    arr : list
        ordered list
    k : float
        value to find in list

    Returns
    -------
    index: int
        the index in list is value k, if k not in list return -1

    """
    min, max, mid = 0, len(arr) - 1, 0
    while min <= max:
        mid = (min + max) // 2
        if arr[mid] > k:
            max = mid - 1
        elif arr[mid] < k:
            min = mid + 1
        else:
            return mid
    return -1
