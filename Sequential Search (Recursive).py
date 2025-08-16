# Define a recursive sequential search function
def sequential_search_rec(a_list, item):

    # Base case: if the list is empty, the item is not found
    if len(a_list) == 0:
        return False

    # If the first element of the list matches the item, return True
    elif a_list[0] == item:
        return True

    else:
        # Call the same function again, but with the rest of the list (excluding the first element)
        return sequential_search_rec(a_list[1:], item)


# -------------------------------
# Create a test list
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]

# Call the function to search for the number 3 in the list
print(sequential_search_rec(test_list, 3))
