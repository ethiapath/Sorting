### helper function
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range( 0, elements ):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


### recursive sorting function
def merge_sort( arr ):
    if len( arr ) > 1:
        left = merge_sort( arr[ 0 : len( arr ) // 2 ] )
        right = merge_sort( arr[ len( arr ) // 2 : ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort( arr, low, high ):
    # base case
    if len(arr) < 2:
        return arr
    else:
        # 1. Select a pivot. Often times this is the first or last element in a set. It can also be the middle.
        pivot = 0 #len(arr) // 2
        # 2. Move all elements smaller than the pivot to the left. 
        smaller = []
        for s in arr[1:]:
            if s < arr[pivot]:
                smaller.append(s)
        # 3. Move all elements greater than the pivot to the right.
        greater = []
        for g in arr[1:]:
            if g > arr[pivot]:
                greater.append(g)
            
        # 4. While LHS and RHS are greater than 1, repeat steps 1-3 on each side.
        return quick_sort(smaller, 0, pivot-1) + [arr[pivot]] + quick_sort(greater, pivot+1, len(greater)-1)

    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(quick_sort(arr1, 0, len(arr1)))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
