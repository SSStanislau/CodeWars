'''
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
'''


def snail(array):
    temp_list = []
    if array and len(array) > 1:
        if isinstance(array[0], list):
            temp_list.extend(array[0])
        else:
            temp_list.append(array[0])
        array.pop(0)
        for lis_index in range(len(array)):
            temp_list.append(array[lis_index][-1])
            array[lis_index].pop(-1)
        if isinstance(array[-1], list):
            temp_list.extend(array[-1][::-1])
        else:
            temp_list.append(array[-1])
        array.pop(-1)
        for lis_index in range(len(array)):
            temp_list.append(array[::-1][lis_index][0])
            array[::-1][lis_index].pop(0)
        temp_list.extend(snail(array))
        return temp_list
    elif array:
        return array[0]
    else:
        return []