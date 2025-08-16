# Define a function to perform insertion sort
def insertion_sort(a_list):

    # Loop from the second element (index 1) to the end of the list
    for index in range(1, len(a_list)):

        # Store the current value to be inserted
        current_value = a_list[index]

        # Set a pointer to the current index
        pos = index

        # Shift elements to the right to make space for current_value
        # Keep shifting as long as current_value is less than the previous element

        while pos > 0 and a_list[pos - 1] > current_value:
            a_list[pos] = a_list[pos - 1]  # Move the larger element one step to the right
            pos = pos - 1  # Move the position pointer to the left

        # Place the current_value in its correct position
        a_list[pos] = current_value


# ------------------------------------
# Define the unsorted list
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Sort the list using insertion sort
insertion_sort(a_list)

# Print the sorted list
print(a_list)
