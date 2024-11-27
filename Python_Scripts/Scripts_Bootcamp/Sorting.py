# Step 1: Create the data list
data = [45, 12, 78, 34, 89, 23, 44, 50, 66, 94]

# Step 2: Create a copy of the data to keep the original list intact
data_copy = data

# Step 3: Implement bubble sort
for i in range(len(data_copy)):
  for j in range(len(data_copy)-i-1):
    if data_copy[j] > data_copy[j+1]:
      data_copy[j], data_copy[j+1] = data_copy[j+1], data_copy[j]

# Step 4: Use Python's built-in sort function on the original list
data_sorted = sorted(data)

# Step 5: Print both sorted lists
print("Bubble sorted list:", data_copy)
print("Python sorted list:", data_sorted)