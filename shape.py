
from pygame import QUIT


def hollowSquare(rows, cha):

	for i in range(1, rows + 1):
		
		# Print stars for each solid rows
		if (i == 1 or i == rows):
			for j in range(1, rows + 1):
				print(cha, end = "")

		# stars for hollow rows
		else:
			for j in range(1, rows + 1):
				if (j == 1 or j == rows):
					print(cha, end = "")
				else:
					print(end = " ")

        

		# Move to the next line/row
		print()
	
# Function for Solid square
def solidSquare(rows, cha):

	for i in range(1, rows):
		
		# Print stars after spaces
		for j in range(1, rows + 1):
			print(cha, end = "")

		# Move to the next line/row
		print()
	
# Utility program to print all patterns
def printPattern(rows, cha, filled):
    if filled == 'y':
        print("\nSolid Square")
        solidSquare(rows, cha)
        
    elif filled == 'n':
        print("\nHollow Square:")
        hollowSquare(rows, cha)
    else:
        print("error occured")


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


def main():

    run = True
    instruction = """\n
    h - to get help
    c - to display circle pattern
    s - to display square pattern (with hallow and filled type)
    q - to quit program
    """
    while run:
        cmd = input('Enter command: ')
        if cmd == 'h':
            print(instruction)
        elif cmd == 'c':
            row = int(input("\nenter rows: "))
            col = int(input('enter cols: '))
            cha = input('enter characters: ')

            circle(row, col, cha)
        elif cmd == 's':
        
            rows = int(input("\nenter amount rows: "))
            cha = input("enter character to draw: ")
            filled = input("filled square - y - yes | n - no? :")
            printPattern (rows, cha, filled)

        elif cmd == 'q':
            run = False

        else:
            print('invalid input')


main()