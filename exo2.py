myTable = [12,6,20,3,15]
for i in range(len(myTable)-1):
    if(myTable[i]>myTable[i+1]):
        stock1 = myTable[i]
        myTable[i] = myTable[i+1]
        myTable[i+1]= stock1

print(myTable)