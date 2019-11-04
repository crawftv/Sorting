# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
# loop through n-1 elements
   for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        h = arr[cur_index]
        n = arr[smallest_index]
        arr[i] = n
        arr[smallest_index] = h
   return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    clear_pass = False
    while clear_pass == False:
        switch_count = 0
        for i in range(0, len(arr) - 1):
            o = arr[i]
            n = arr[i + 1]
            if n < o:
                switch_count += 1
                arr[i] = n
                arr[i + 1] = o
        if switch_count == 0:
            clear_pass = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
