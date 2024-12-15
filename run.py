# Bubble Sort Algorithm with Explanations
def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm.
    
    Args:
        arr (list): List of elements to be sorted (numbers).
        
    Returns:
        list: Sorted list.
    """
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Flag to check if any swapping occurred
        swapped = False
        # Compare adjacent elements
        for j in range(0, n-i-1):
            # If the element is greater than the next, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, break early
        if not swapped:
            break
    return arr

# Test the algorithm with explanations
def test_sorting_algorithm():
    """
    Tests the Bubble Sort algorithm with sample data and provides explanations.
    """
    # Sample input array
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)

    # Apply Bubble Sort
    sorted_array = bubble_sort(test_array)

    # Output the sorted array
    print("Sorted array:", sorted_array)

    # Explanation of the process
    print("\nExplanation:")
    print("1. Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.")
    print("2. This process is repeated for all elements except the last sorted elements in each iteration.")
    print("3. If no swaps are needed in a pass, the algorithm stops early, as  list is already sorted.")

# Run the test
test_sorting_algorithm()
