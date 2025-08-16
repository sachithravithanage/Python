# Define a function to perform selection sort
def selection_sort(a_list):

    # Outer loop: from the last index to the first (backward)
    for j in range(len(a_list) - 1, 0, -1):

        # Start by assuming the first element is the largest
        pos_of_max = 0

        # Inner loop: find the position of the largest element in unsorted part
        for i in range(1, j + 1):

            # If a larger element is found, update pos_of_max
            if a_list[i] > a_list[pos_of_max]:
                pos_of_max = i

        # After finding the largest, swap it with the element at current end position (j)
        temp = a_list[j]
        a_list[j] = a_list[pos_of_max]
        a_list[pos_of_max] = temp


# ----------------------------------
# Define the unsorted list
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Sort the list using selection sort
selection_sort(a_list)

# Print the sorted list
print(a_list)
