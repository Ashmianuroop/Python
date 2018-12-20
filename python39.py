def max_num_in_list( list ):
    max = list[ 0 ]
    for p in list:
        if p > max:
            max = p
    return max
print(max_num_in_list([1, 2,3,-9,-7,4,5,-1 -8, 0]))
