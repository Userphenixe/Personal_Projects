def find_pairs(numbers, target):
  # Initialize a list to store pairs
  pairs = []
  # Outer loop to select the first number
  for i in range(len(numbers)):
      # Inner loop to select the second number
      for j in range(i + 1):
          # Check if the two numbers add up to the target
          if numbers[i] + numbers[j]  == target:
              pairs.append((numbers[i], numbers[j]))
  return pairs

# Test the function with example data
numbers = [2, 4, 3, 5, 7]
target = 9
print(f"Pairs that sum to {target}: {find_pairs(numbers, target)}")