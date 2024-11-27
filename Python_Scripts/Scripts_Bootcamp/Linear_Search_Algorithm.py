def linear_search_index(my_list, item):
  # TODO: write the function
  i = 0
  Found = False
  while i < len(my_list) and Found == False:
    if my_list[i] == item:
      Found = True
      return Found, i
      break
    else:
      i += 1
  return Found, None
# Test the function
print(linear_search_index([5, 8, 12, 7, 6, 18], 12))
print(linear_search_index([5, 8, 12, 7, 6, 18], 3))