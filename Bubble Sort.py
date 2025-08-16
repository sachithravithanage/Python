# Define the bubble_sort function that takes a list as input
def bubble_sort(a_list):

    # Outer loop: controls how many passes (from end of list to start)
    for j in range(len(a_list) - 1, 0, -1):

        # Inner loop: compares each adjacent pair in the unsorted part
        for i in range(j):

            # If the current item is greater than the next one, swap them
            if a_list[i] > a_list[i + 1]:

                # Swap the elements
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp


# -------------------------------------------
# Define the unsorted list
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Call the bubble_sort function to sort the list
bubble_sort(a_list)

# Print the sorted list
print(a_list)
