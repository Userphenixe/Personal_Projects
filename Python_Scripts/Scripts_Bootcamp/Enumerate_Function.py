def odd_indexed_elements(my_list):
    # Initialize an empty list to store elements at odd indices
    my_list_odd = []
    dictio = {}

    # Use enumerate to loop through my_list, with index and value for each element
    for index, value in enumerate(my_list):
        dictio[index] = value  # Store the value at its index as key in dictio

    # Extract elements from odd indices and store them in my_list_odd
    for key, value in dictio.items():
        if int(key) % 2 != 0:
            my_list_odd.append(value)

    return my_list_odd  # Return list of elements at odd indices


# Test the function
liste = odd_indexed_elements([10, 20, 30, 40, 50, 60])
print(liste)  # Expected output: [20, 40, 60]