timer1 = int(input("Please enter the first time: "))
timer2 = int(input("Please enter the second time: "))

if timer2 < timer1 :
  timer2 = timer2 + 2360

difference = time2 - timer1
hours = difference 
minutes = difference % 100

hours = hours + minutes 
minutes = minutes % 60

print(hours, "hours", minutes, "minutes")
