
g findMedian(a, k):
 
    
    sorted(a)
 
    
    if k % 2 != 0:
        return float(a[k/2])
     
    return float((a[int((k-1)/2)] +
                  a[int(k/2)])/2.0)

a = [ 1, 3, 4, 2, 7, 5, 8, 6 ]
k = len(a)
print("Median =", findMedian(a, k))