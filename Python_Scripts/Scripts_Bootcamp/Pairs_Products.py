def find_pair_with_product(nums, target_product):
    # Initialize an empty dictionary to store numbers and their indices
    d = {}

    # Iterate over each number in the list
    for i in range(len(nums)):

        # Check if there exists a required pair in the dictionary
        if target_product % nums[i] == 0:  # Ensure target_product is divisible by num
            if target_product // nums[i] in d:
                return [d[target_product // nums[i]], i]

        # Add the current number and its index to the dictionary
        d[nums[i]] = i

    # If no such pair exists, return -1
    return -1


# Test the function
print(find_pair_with_product([2, 4, 1, 6, 5, 10], 20))
print(find_pair_with_product([3, 8, 12, 5, 9], 45))
print(find_pair_with_product([2, 3, 4, 7], 15))