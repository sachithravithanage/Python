# Function to heapify a subtree rooted at index i
# n is the size of the heap
def heapify(a_list, n, i):
    # Assume the current index i is the largest
    largest = i

    # Left child index of node i
    l = 2 * i + 1

    # Right child index of node i
    r = 2 * i + 2

    # If left child exists and is greater than root, update largest
    if l < n and a_list[l] > a_list[largest]:
        largest = l

    # If right child exists and is greater than current largest, update largest
    if r < n and a_list[r] > a_list[largest]:
        largest = r

    # If the largest is not the root node, swap and continue heapifying
    if largest != i:
        # Swap current node with the largest child
        a_list[i], a_list[largest] = a_list[largest], a_list[i]

        # Recursively heapify the affected subtree
        heapify(a_list, n, largest)

# Function to perform heap sort
def heap_sort(a_list):
    n = len(a_list)

    # Step 1: Build a max heap from the list
    # Start from the last parent node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(a_list, n, i)

    # Step 2: One by one, remove elements from the heap
    for i in range(n - 1, 0, -1):
        # Swap the current root (max element) with the last element
        a_list[i], a_list[0] = a_list[0], a_list[i]

        # Reduce the heap size and heapify the new root
        heapify(a_list, i, 0)


# ------------------------------------------------
# Define the list to be sorted
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Call the heap_sort function to sort the list
heap_sort(a_list)

# Print the final sorted list
print(a_list)
