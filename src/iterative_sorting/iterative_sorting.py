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
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# int_arr = [1, 5, 6, 2, 8, 7, 4, 9, 3]
# print(selection_sort(int_arr))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    did_swap = True
    while did_swap:
        did_swap = False
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                temp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = temp
                did_swap = True

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(bubble_sort(arr1))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr