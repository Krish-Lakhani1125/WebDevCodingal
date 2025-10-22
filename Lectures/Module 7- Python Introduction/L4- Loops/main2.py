n = int(input("Enter the number of rows: "))
#Outer loop for ech row
for i in range(1, n+1):
    #inner loop for each column in the row
    for i in range(i):
        #Print star, end with space instead of new line
        print('*', end=' ')
        #After each row, print a new line
    print()
