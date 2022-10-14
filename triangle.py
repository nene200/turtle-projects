def triangle(n, cha):
    k = n - 1

    # outer loop to handle number of rows
    for i in range(0, n):

        # inner loop to handle number of spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

        # decrementing k after each loop
        k = k - 1

        # inner loopto handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
            
            # printing characters
            print(cha +' ', end="")

        # ending line after each row
        print("\r")
n = int(input("enter n: "))
cha = input("enter character: ")
triangle(n, cha)

