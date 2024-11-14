def two_sum(target, *args):
    if target <= 0:
        print("Please enter a valid target!")
    else:
        for i in range(len(args)):
            for j in range(i + 1, len(args)):
                if args[i] + args[j] == target:
                    return [args[i], args[j]]
    return None  # Return None if no pairs are found

# Pass individual numbers as arguments instead of a list
result = two_sum(10, 7, 4, 3, 1, 8)
print(result)
