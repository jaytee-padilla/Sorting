# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for x in range(cur_index, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x

        # TO-DO: swap
        # temp variable will hold the value of what's in the current index
        # the value of cur_index is overwritten by the smallest_index's value, so the temp is needed to record the value of cur_index before it's overwritten
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    # return the sorted array/list
    return arr


# TO-DO:  implement the Bubble Sort function below
# Loop through array
# Compare each element to its neighbor
# If elements in wrong position (relative to each other, swap them)
# If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
def bubble_sort( arr ):
    for i in range(0, len(arr - 1)):
        print(arr[i])

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


print(selection_sort([5, 10, 3, 30, 75, 90, 11, 69]))
print(bubble_sort([5, 10, 3, 30, 75, 90, 11, 69]))