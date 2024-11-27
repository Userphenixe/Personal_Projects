def binary_search_recursive(my_list, item):
  # TODO: Write a binary search function using recursion
  # Assume that the provided list is sorted (in ascending order)
  Found = False
  First = 0
  Last = len(my_list) -1
  while Found == False and First < len(my_list):
    midpoint = (First + Last) // 2
    if my_list[midpoint] == item:
      Found = True
      return Found
      break
    else:
      if my_list[midpoint] < item:
        my_list[First] += 1
      else:
        my_list[Last] -= 1
    return False
# Testing the function
print(binary_search_recursive([1, 3, 5, 7, 9], 5))
print(binary_search_recursive([1, 3, 5, 7, 9], 6))