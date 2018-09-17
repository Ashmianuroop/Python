t = float(input("Input time in seconds: "))
d = time // (24 * 3600)
t = time % (24 * 3600)
h = time // 3600
t %= 3600
m = time // 60
t %= 60
s = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

