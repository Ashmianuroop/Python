f merge_two(a, b):
    (m, n) = (len(a), len(b))
    i = j = 0
 
    
    d = []
 
    
    while i < m and j < n:
        if a[i] <= b[j]:
            d.append(a[i])
            i += 1
        else:
            d.append(b[j])
            j += 1
 

    while i < m:
        d.append(a[i])
        i += 1
 
    
    while j < n:
        d.append(b[j])
        j += 1
 
    return d
 
f merge(a, b, c):
    t = merge_two(a, b)
    return merge_two(t, c)
 
if __name__ == "__main__":
    A = [1, 2, 3, 5]
    B = [6, 7, 8, 9]
    C = [10, 11, 12]
    print(merge(A, B, C))
