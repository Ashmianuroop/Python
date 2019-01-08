h5 = input("Enter String: ")
if len(h) % 2 == 0:

   print(h[len(h) // 2 - 1] + h5[len(h) // 2])
   k=h5.replace( h5[len(h5) // 2 - 1],"*")
   print(k.replace(h5[len(h5) // 2 ],"*"))

else:

   print(h5.replace(h5[len(h5) // 2],"*"))
