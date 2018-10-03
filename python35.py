print("Enter 'k' for exit.");
string = input("Enter any string to count character: ");
if string == 'k':
    exit();
else:
    char = input("Enter a character to count to count from above string: ");
    val = string.count(char);
    print("Total = ",val);