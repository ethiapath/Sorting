# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    if len(arr) == 0:
        return []

    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):

    # check for empty array
    if len(arr) == 0:
        return []

    items = [arr[0]]
    unsorted_start = 1
    for i in range(unsorted_start, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            swap = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = swap
            j = j-1

    return arr

# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    swaped = True
    while swaped:
        swaped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                swaped = True
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
    return arr
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
