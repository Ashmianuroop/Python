Mname = input("Enter file name: ")
k = 0
 
with open(Mname, 'r') as M:
    for line in M:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isspace):
                    k=k+1
print("Occurrences of blank spaces:")
print(k)