# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( left_arr, right_arr ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO
    left_index, right_index = 0, 0
    merged_arr = []

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merged_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merged_arr.append(right_arr[right_index])
            right_index += 1

    merged_arr += left_arr[left_index:]
    merged_arr += right_arr[right_index:]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element 
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled
def merge_sort( arr ):
    # TO-DO
    # if length of arr is <= 1, the arr is technically sorted at that point because there's nothing else in the arr
    if len(arr) <= 1:
        return arr

    # if the length of arr is greater than 1, that means arr needs to continue being split until it is only a single element
    # to continuously split the arr into a series of single elements, merge_sort is invoked via recursion
    half = len(arr) // 2
    # grab elements from index 0 to the middle of the list
    left = merge_sort(arr[:half])
    # grab elements from middle of the list to the last index
    right = merge_sort(arr[half:])

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

print(merge_sort([69, 100, 2, 8, 3, 5, 77, 666]))