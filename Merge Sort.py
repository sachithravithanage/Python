# Define the merge_sort function
def merge_sort(a_list):

    # Print the current list to show the split phase
    print("Splitting ", a_list)

    # Base case: only proceed if the list has more than 1 element
    if len(a_list) > 1:

        # Find the middle index to split the list
        mid = len(a_list) // 2

        # Create left and right halves
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        # Recursively sort the left half
        merge_sort(left_half)
        # Recursively sort the right half
        merge_sort(right_half)

        # Initialize indices for merging
        i = 0  # index for left_half
        j = 0  # index for right_half
        k = 0  # index for original list (a_list)

        # Merge the two sorted halves into a_list
        while i < len(left_half) and j < len(right_half):

            # If left element is smaller, add it to a_list
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1

            else:
                # Else, add the right element
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1  # Move to the next position in a_list

        # Copy any remaining elements from left_half
        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        # Copy any remaining elements from right_half
        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1

    # Print the current list to show the merge phase
    print("Merging ", a_list)


# --------------------------------------------
# Define the unsorted list
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Call merge_sort to sort the list
merge_sort(a_list)

# Print the final sorted list
print(a_list)
