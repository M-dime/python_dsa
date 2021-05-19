"""
1. Bubble sort  5 3 8 7
             3 5 8 7
             3 5 7 8

Time complexity = O(n^2)
space complexity = O(1)
----------------------------------------------####################################################----------------------------------------------------------
2. selection Sort
select the min and swap it with left most element of unsorted list
 4 6 2 8 7
2| 6 4 8 7
2 4| 6 8 7
2 4 6| 8 7
2 4 6 7| 8
2 4 6 7 8|

time complexity = O(n**2)
space complexity = O(1)
----------------------------------------------####################################################----------------------------------------------------------
3. Insertion Sort
divide the given array in sorted and unsorted sublist
we insert the element in sorted list one by one untill reach the last and then sort it

3 2 5 7 4
3| 2 5 7 4
3 2| 5 7 4 => 2 3| 5 7 4
2 3 5| 7 4 => 2 3 5| 7 4
2 3 5 7| 4 => 2 3 5 7| 4
2 3 5 7 4| => 2 3 5 4 7| => 2 3 4 5 7|

time complexity = O(n**2)
space complexity = O(1)
----------------------------------------------####################################################----------------------------------------------------------
4. Quick sort


"""
def Bubble_sort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

def selection_sort(arr):
    for i in range(0,len(arr)-1):
        imin = i
        for j in range(i+1,len(arr)):
            if arr[j]< arr[imin]:
                imin = j
        if imin != i:
            arr[imin], arr[i] = arr[i], arr[imin]
    return arr

def Insertion_sort(arr):
    for i in range(len(arr)):
        val_to_sort = arr[i]
        while arr[i-1]>val_to_sort and i>0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i-1
    return arr


if __name__ == '__main__':
    arr = [1,4,3,9,6,7,4,5,2]
    print(Bubble_sort(arr))
    print(selection_sort(arr))
    print(Insertion_sort(arr))