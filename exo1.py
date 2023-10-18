myTable = [12,6,20,3,15]

stock1 = myTable[0]
myTable[0] = myTable[1]
myTable[1]= stock1

print(myTable)
# Ca permute bien ma premiere et deuxieme case.