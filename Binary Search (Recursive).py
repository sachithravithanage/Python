# Define a recursive binary search function that takes a sorted list and the item to search
def binary_search_rec(a_list, item):

    # Base case: if the list is empty, the item is not found
    if len(a_list) == 0:
        return False

    else:
        # Find the middle index of the current list
        mid = len(a_list) // 2

        # If the middle element is the item, return True
        if a_list[mid] == item:
            return True

        else:
            # If item is smaller than middle element, search in the left half
            if item < a_list[mid]:
                return binary_search_rec(a_list[:mid], item)  # left half (excluding mid)

            else:
                # If item is greater than middle element, search in the right half
                return binary_search_rec(a_list[mid + 1:], item)  # right half (excluding mid)

# -------------------------------
# Create a sorted test list
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]

# Call the recursive binary search function to look for number 3 in the test_list
print(binary_search_rec(test_list, 3))
