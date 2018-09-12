str = 'd123'
str = '123'
try:
    k = float(str)
except (ValueError, TypeError):
    print('nNot numeric')
print()