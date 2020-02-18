# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    i = 0
    j = 0
    k = 0
    while i <= elements:
        if j < len(arrA) and k < len(arrB) and arrA[j] <= arrB[k]:
            merged_arr[i] = arrA[j]
            j += 1
        elif j < len(arrA) and k < len(arrB) and arrA[j] > arrB[k]:
            merged_arr[i] = arrB[k]
            k += 1
        elif j == len(arrA) and k < len(arrB):
            merged_arr[i] = arrB[k]
            k += 1
        elif j < len(arrA) and k == len(arrB):
            merged_arr[i] = arrA[j]
            j += 1
        i += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    mid = len(arr) // 2
    if len(arr[:mid]) > 1:
        arr[:mid] = merge_sort(arr[:mid])
    if len(arr[mid:]) > 1:
        arr[mid:] = merge_sort(arr[mid:])
    return merge(arr[:mid], arr[mid:])


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
