def selection_sort(arr):
     # Make a copy of the list to avoid modifying the original
    lst = arr.copy()
    n = len(lst)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    
    return lst

# Example usage:
if __name__ == "__main__":
    unsorted_list = [64, 25, 12, 22, 11]
    sorted_list = selection_sort(unsorted_list)
    print("Sorted list:", sorted_list)