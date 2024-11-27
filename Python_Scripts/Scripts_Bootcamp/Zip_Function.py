# Provided lists of numbers and letters
numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c', 'd']

# Step 1: Combine numbers and letters lists
combined_list = list(zip(numbers, letters))
print("Combined list of numbers and letters:", combined_list)

# Step 2: Unpack combined_list into two separate lists
unpacked_numbers, unpacked_letters = zip(*combined_list)
print("Unpacked list of numbers:", unpacked_numbers)
print("Unpacked list of letters:", unpacked_letters)