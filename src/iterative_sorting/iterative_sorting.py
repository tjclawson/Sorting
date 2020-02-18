# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    did_swap = True
    while did_swap:
        did_swap = False
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i -1] = arr[i - 1], arr[i]
                did_swap = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return arr

    maximum = max(arr)
    count_arr = [0] * (maximum + 1)
    for num in arr:
        count_arr[num - 1] += 1
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"

    original_length = len(arr)
    arr.clear()
    for i in range(0, original_length):
        arr.extend([i] * count_arr[i])

    return arr
