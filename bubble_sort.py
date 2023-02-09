
def bubble_sort(arr):
    # Get the length of the list
    n = len(arr)

    # Repeat the outer loop n-1 times
    for i in range(n - 1):
        # Initialize a flag to track whether any swaps have been made
        swap = False

        # Repeat the inner loop n-1-i times
        for j in range(n - 1 - i):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set the flag to indicate that a swap has been made
                swap = True

        # If no swaps have been made in the inner loop, the list is already sorted
        # and we can break out of the outer loop
        if not swap:
            break

    # Return the sorted list
    return arr


def main():
    # Test array
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)

    # Call the bubble sort function
    arr = bubble_sort(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()