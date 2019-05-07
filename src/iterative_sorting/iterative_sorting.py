nums = [3, 5, 6, 1, 4, 2]

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        smallest_index = cur_index
    return arr


print(selection_sort(nums))
# O() = O(n^2)

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    count = 0
    cycle = True
    while cycle:
        for i in range(0, len(arr)-1):
            if arr[i+1] < arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count += 1
        if count == 0:
            cycle = False
        count = 0
    return arr


print(bubble_sort(nums))


# STRETCH: implement the Count Sort function below

def count_sort(arr, maximum=-1):

    return arr