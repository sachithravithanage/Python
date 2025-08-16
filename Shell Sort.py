# Define the shell_sort function that sorts the list
def shell_sort(a_list):

    # Start with a big gap and reduce it each time
    sublist_count = len(a_list) // 2

    # Continue until the gap becomes 0
    while sublist_count > 0:

        # Perform a gapped insertion sort for each starting point in the sublist
        for start_pos in range(sublist_count):

            # Sort the sublist starting at start_pos and going by steps of gap = sublist_count
            gap_insertion_sort(a_list, start_pos, sublist_count)

        # Print the list after sorting with the current gap size
        print("After increments of size", sublist_count, "the list is", a_list)

        # Reduce the gap for the next pass
        sublist_count = sublist_count // 2

# Helper function that performs insertion sort on elements with a specific gap
def gap_insertion_sort(a_list, start, gap):

    # Loop over elements in the sublist
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        pos = i

        # Shift elements until the correct location for current_value is found
        while pos >= gap and a_list[pos - gap] > current_value:
            a_list[pos] = a_list[pos - gap]
            pos = pos - gap

        # Place current_value in the correct location
        a_list[pos] = current_value


# -----------------------------
# Example unsorted list
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Call shell_sort to sort the list
shell_sort(a_list)

# Print the final sorted list
print(a_list)
