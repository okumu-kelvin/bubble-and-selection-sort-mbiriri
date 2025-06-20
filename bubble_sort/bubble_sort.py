def bubble_sort(unsorted_list):
   # Make a copy of the list to avoid modifying the original
    lst = unsorted_list.copy()
    n = len(lst)
    
    # Traverse through all list elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    
    return lst


 #Example usage: 
if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(unsorted_list)                
    print("Sorted list:", sorted_list)