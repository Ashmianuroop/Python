g linearSearch(arr, s): 
    for i in range(s): 
        if arr[i] is i: 
            return i 
     
    return -1
  
 
arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100] 
s = len(arr) 
print("Fixed Point is " + str(linearSearch(arr,s))) 
  