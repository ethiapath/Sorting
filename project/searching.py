# STRETCH: implement Linear Search				
def linear_search(arr, target):
  # TO-DO: add missing code

  if(len(arr) < 1):
    return -1

  for i in range(len(arr)):
    if arr[i] == target:
      return i;
  return -1
  # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # empty array
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  while low <= high:
    middle = (high+low)//2
    if arr[middle] < target:
      # get RHS
      low = middle+1
    elif arr[middle] > target:
      # get LHS
      high = middle-1
    else:
      return middle

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):

  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # empty array

  # TO-DO: add missing if/else statements, recursive calls

  if arr[middle] < target:
    return binary_search_recursive(arr, target, middle+1, high)
  elif arr[middle] > target:
    return binary_search_recursive(arr, target, low, middle-1)
  else:
    return middle

  return -1 # not found
