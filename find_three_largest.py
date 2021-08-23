result = []

def findThreeLargestNums(array):
    i = 0
    while i < 3:
        result.append(max(array))
        indexNum = array.index(result[i])
        array.pop(indexNum)
        i += 1
    return sorted(result)

print(findThreeLargestNums(array))

def find_max(array):
    max_nums = []
    while len(max_nums) < 3:
        x = int(max(array))
        max_nums.append(x)
        array.remove(x)
        max_nums.sort()
    return max_nums

def threeLargest(array):
    result = []
    for i in range(3):
        temp = max(array)
        result.append(temp)
        array.remove(temp)
    return result[::-1]


array = [[141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7], [8, 8, 8, 8, 8, 8, 8, 8, 10, 8, 8, 8, 8, 8], [1, 1, 1, 1, 1, 1, 1, 1]]
for x in array:
    print(threeLargest(x))

def find_largest(arr):
    new_list= []

    while len(new_list) < 3:
        for i in arr:
            if i == max(arr):
                new_list.append(i)
                arr.remove(i)
                break
    print(sorted(new_list))

    return sorted(new_list)

find_largest([1, 1, 1, 1, 1, 1, 1, 1])

def find_three_largest_numbers1(array):
    result = array[0:3]
    for a in array[3:]:
        if a > min(result):
            result[result.index(min(result))] = a
    return result
def find_three_largest_numbers2(array):
    result = []
    for a in range(3):
        max = array[0]
        for b in array:
            if b > max:
                max = b
        array.remove(max)
        result.insert(0, max)
    return result

from math import inf

#Our one *

def find_largest(my_list):
    largest = [-inf, -inf, -inf]

    for item in my_list:
        if item > largest[2]:
            largest[2], largest[1], largest[0] = item, largest[2], largest[1]
        elif item > largest[1]:
            largest[1], largest[0] = item, largest[1]
        elif item > largest[0]:
            largest[0] = item
    
    return largest

def main():
    # # CASE 1
    array1 = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    # result = [18, 141, 541]

    # # CASE 2
    array2 = [8, 8, 8, 8, 8, 8, 8, 8, 10, 8, 8, 8, 8, 8]
    # result = [8, 8, 10]

    # # CASE 3
    array3 = [1, 1, 1, 1, 1, 1, 1, 1]
    # result = [1, 1, 1]
    print(find_largest(array1))
    print(find_largest(array2))
    print(find_largest(array3))

if __name__ == "__main__":
    main()
