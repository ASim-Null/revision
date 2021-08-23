"""
So it doesn't actually skip the first element - minimum = indx  sets the first element as the assumed minimum. 
for elem in range(indx + 1, len(arr)) then loops over all of the remaining elements, and if it finds a value that's smaller 
than the first element, will update minimum . Does that make sense?
:raised_hands:

Heather Cartwright (they/them)  11 days ago
So if you have a list mylist = [8, 3, 5, 1, 4, 7, 2, 6]  and pass it into the function the function will set minimum to 8. 
Then it'll iterate through the loop: 3 is smaller than 8, so immediately minimum is updated. 
Then it checks 5, which isn't, so it'll pass over that, then 1 which is the smallest in the list, so minimum gets updated again. 
It finishes checking the list and of course minimum doesn't get updated again because 1 is the smallest, and the last bit of the 
function swaps the places of 1 and 8, so when you print the list at the end, you'll end up with [1, 3, 5, 8, 4, 7, 2, 6]
"""
def selection_sort(arr):
    for indx in range(len(arr)):
        minimum = indx

        for elem in range(indx + 1, len(arr)):
            # Select the smallest value
            if arr[elem] < arr[minimum]:
                minimum = elem
                # print(minimum)

        # Place it at the front of the
        # sorted end of the array
        arr[minimum], arr[indx] = arr[indx], arr[minimum]
        # print(arr)

    return arr
