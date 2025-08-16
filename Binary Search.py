# Define a function for binary search which takes a sorted list and the item to search
def binary_search(a_list, item):

    # Start index of the list
    first = 0

    # End index of the list
    last = len(a_list) - 1

    # Flag to check if the item is found
    found = False

    # Loop as long as the search area is valid and item not yet found
    while first <= last and not found:

        # Find the middle index of the current search range
        mid = (first + last) // 2

        # Check if the middle element is the item
        if a_list[mid] == item:

            # Item found
            found = True

        else:
            # If the item is smaller than the middle, search in the first half
            if item < a_list[mid]:
                last = mid - 1  # move end to mid - 1

            else:
                # If the item is greater, search in the second half
                first = mid + 1  # move start to mid + 1

    # After loop, if found is True, return the index (mid)
    if found:
        return mid

    else:
        # If not found, return -1
        return -1


# -----------------------------
# Create a sorted test list
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]

# Call the binary_search function to search for number 3 in the test_list
print(binary_search(test_list, 3))
