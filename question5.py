"""
UMass ECE 241 - Advanced Programming
Homework #2     Fall 2018
question5.py - 3 way merge sort
"""


## This is an example of code to merge two lists in a descending order
## You can directly call this function or write your own one

# The two lists "lefthalf" and "righthalf" are start from i and j
# The destination list "alist" start from the given position "pos"
# The function returns the number of comparisons during merge
def merge2List(alist, lefthalf, righthalf, i, j, pos):

    comparison = 0 # initial the comparison number as 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[pos] = righthalf[j]
            j += 1
        else:
            alist[pos] = lefthalf[i]
            i += 1
        comparison += 1
        pos += 1

    while i < len(lefthalf): # add the remained numbers in the lefthalf to alist
        alist[pos] = lefthalf[i]
        i = i + 1
        pos += 1

    while j < len(righthalf): # add the remained numbers in the righthalf to alist
        alist[pos]=righthalf[j]
        j=j+1
        pos += 1

    return comparison


# Implement 3 way merge sorting algorithm
# It takes a given list "alist" and return the number of comparison used
def mergeSort_3_way(alist):
    comparison = 0
    if len(alist) > 1:
        length = len(alist)
        # the two "midpoints" are as follows
        mid1 = int(length / 3)
        mid2 = mid1 * 2

        if len(alist) > 2:
            # for lists with more than 2 elements
            length = len(alist)
            mid1 = int(length / 3)
            mid2 = mid1 * 2
        elif len(alist) == 2:
            # when a list has just 2 element
            length = len(alist)
            mid1 = 0 # mid points are hardcoded such that there exists one empty array
            mid2 = 1
        # elements are split into three arrays as follows
        alist1 = alist[:mid1]
        alist2 = alist[mid1:mid2]
        alist3 = alist[mid2:]

        # recursive calls for merge sort
        comparison += mergeSort_3_way(alist1)
        comparison += mergeSort_3_way(alist2)
        comparison += mergeSort_3_way(alist3)

        # positions of the three lists and the position pos of the final result alist
        i = 0
        j = 0
        k = 0
        pos = 0
        # checking conditions to merge with sorting
        while i < len(alist1) and j < len(alist2) and k < len(alist3):
            if alist1[i] < alist2[j]:
                if alist2[j] < alist3[k]:
                    alist[pos] = alist3[k]
                    k += 1
                else:
                    alist[pos] = alist2[j]
                    j += 1
            elif alist1[i] > alist2[j]:
                if alist1[i] > alist3[k]:
                    alist[pos] = alist1[i]
                    i += 1
                else:
                    alist[pos] = alist3[k]
                    k += 1
            comparison += 2
            pos += 1
        # code to cater to lists when one of the lists have run out. The given function is called
        if i == len(alist1):
            comparison += merge2List(alist, alist2, alist3, j, k, pos)
        elif j == len(alist2):
            comparison += merge2List(alist, alist1, alist3, i, k, pos)
        else:
            comparison += merge2List(alist, alist1, alist2, i, j, pos)
    return comparison

