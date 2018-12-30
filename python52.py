import inflect
a = int(input("enter a number: "))
p = inflect.engine()

words = p.number_to_words(a)

print(words) 