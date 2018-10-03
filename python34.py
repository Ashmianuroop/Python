def paragraph_lengthy(pname):
        with open(pname) as p:
                for i, l in enumerate(p):
                        pass
        return i + 1
print("Number of lines in the paragraph: ",paragraph_lengthy("test.txt"))
