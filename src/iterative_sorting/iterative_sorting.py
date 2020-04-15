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
        # temp = arr[cur_index]
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        # arr[smallest_index] = temp
    # return the sorted array/list
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # perform initial bubble sort of array if possible
    # if no values were swapped during initial pass through, the array is already sorted
    # if no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
    # bubble sort will continue as long as there has been at least 1 swap of values
    swapped = True
    # copy current version of the arr into temp_arr, this will be used to check if any swapping in the array has been done
    temp_arr = arr.copy()

    while swapped:
        for i in range(0, len(arr) - 1):
            cur_index = i
            cur_index_neighbor = i + 1
            temp_value = arr[cur_index]

            # if the value of the current index is greater than the value of its neighbor, swap the two values
            if arr[cur_index] > arr[cur_index_neighbor]:
                arr[cur_index] = arr[cur_index_neighbor]
                arr[cur_index_neighbor] = temp_value

        # after array has been looped through, check if temp_arr (the initial version of the arr) is the same as the newly sorted arr
        # if the arrays are different, a swap has been performed, so the bubble sort needs to run again
        if temp_arr == arr:
            swapped = False
        else:
            temp_arr = arr.copy()

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


# print(selection_sort([5, 10, 3, 30, 75, 90, 11, 69]))
print(bubble_sort([5, 10, 3, 30, 75, 90, 11, 69]))