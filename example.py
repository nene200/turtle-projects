def circle(row, col, cha):

    for i in range(0, row):
        for j in range(0, col):
            if ((j == 0 or j == col-1) and (i!=0 and i!=row-1)):
                print(cha, end = '')
            elif(((i==0 or i==row-1) and (j>0 and j<col-1))):
                print(cha, end='')
            else:
                print(end=' ')

        print()

run = True
while run:
    row = int(input("\nenter rows: "))
    col = int(input('enter cols: '))
    cha = input('enter characters: ')

    circle(row, col, cha)