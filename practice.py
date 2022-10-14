# Python3 program to print
# hollow and solid square patterns

# Function for hollow square


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





run = True
while run:
    # Driver Code
    rows = int(input("\nenter amount rows: "))
    cha = input("enter character to draw: ")
    filled = input("filled square - y - yes | n - no? :")
    printPattern (rows, cha, filled)

    cont = input("\nDo you want to continue? y-yes | n-no: ").lower()
    if cont == "y":
        continue
    elif cont == "n":
        print("Thank you for using our program")
        run = False
    else:
        print("\ninvalid input")
        print("programming restarting")
        continue

    # This code is contributed by
    # Mohit kumar 29
