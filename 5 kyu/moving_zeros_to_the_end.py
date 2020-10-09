'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
'''


def move_zeros(array):
    n = len(array)
    for i in range(n): 
        for j in range(0, n-i-1): 
            if array[j]==0:
                if str(array[j])!='False':
                    array[j], array[j+1]=array[j+1], array[j]
    return array
            