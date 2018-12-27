string=str(input("Enter String 1")).split(" ")
if string[0]==string[1]:
  print(string)
elif string[0]>string[1]:
  print(string[0])
elif string[0]<string[1]:
  print(string[1])
