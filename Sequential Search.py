# Define a function called sequential_search that takes a list and an item to search for
def sequential_search(a_list, item):

    # Start checking from position 0
    pos = 0

    # Set a flag to keep track of whether the item is found
    found = False

    # Loop through the list while we have not reached the end and the item is not found
    while pos < len(a_list) and not found:

        # Check if the current element is equal to the item we are searching
        if a_list[pos] == item:

            # If item is found, set the found flag to True
            found = True

        else:
            # Otherwise, move to the next position
            pos = pos + 1

    # After the loop, if the item was found
    if found:

        # Return the position where it was found
        return pos

    else:
        # If not found, return -1
        return -1

# -----------------------------
# Create a test list of numbers
test_list = [0, 1, 2, 8, 13, 3, 19, 32, 42]

# Call the sequential_search function to look for number 3 in test_list
print(sequential_search(test_list, 3))
