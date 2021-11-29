names = []
x = 0
while x < 10:
	acceptedName = input("enter the name of the next person: ")
    names.append(acceptedName)
    x = x + 1
    
print("Here is are the names in order of the line: ")

while len(names): 
	print (names.pop(0))
