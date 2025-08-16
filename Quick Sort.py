# Main function to perform quick sort on a_list between indices first and last
def quick_sort(a_list, first, last):

    # Only sort if the list section has more than one element
    if first < last:

        # Partition the list and get the position of the pivot
        split_point = partition(a_list, first, last)

        # Recursively sort the left part
        quick_sort(a_list, first, split_point - 1)
        # Recursively sort the right part
        quick_sort(a_list, split_point + 1, last)

# Function to partition the list around a pivot
def partition(a_list, first, last):

    # Choose the first element as the pivot
    pivot_value = a_list[first]

    # Set up markers for scanning from both ends
    left_mark = first + 1
    right_mark = last

    # Loop until the pointers cross
    done = False
    while not done:

        # Move left marker to the right as long as elements are <= pivot
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        # Move right marker to the left as long as elements are >= pivot
        while right_mark >= left_mark and a_list[right_mark] >= pivot_value:
            right_mark = right_mark - 1

        # If markers cross, we're done
        if right_mark < left_mark:
            done = True
        else:
            # Swap elements at left_mark and right_mark
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp

    # After loop, swap pivot with element at right_mark
    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp

    # Return the final position of the pivot
    return right_mark


# --------------------------------------------------
# Create an unsorted list
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Call quick_sort on the full list
quick_sort(a_list, 0, len(a_list) - 1)

# Print the sorted list
print(a_list)
