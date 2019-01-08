c4 = input("Enter String: ")
if len(c4) % 2 == 0:

   print(c4[len(c4) // 2 - 1] + c4[len(c4) // 2])
   k=c4.replace( c4[len(c4) // 2 - 1],"*")
   print(k.replace(c4[len(c4) // 2 ],"*"))

else:

   print(c4.replace(c4[len(c4) // 2],"*"))
