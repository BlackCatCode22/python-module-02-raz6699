def largestOfThree(a, b, c) :
    if a > b:
        # b is smaller
        if a > c:
            # c is smaller
            large = a
        else:
            # a is smaller
            large = c
    else:
        #  a is smaller
        if b > c:
            # c is smaller
            large = b
        else:
            # b is smaller
            large = c
    return large

# Program to Findout The Biggest of 3 Numbers Using Nested if
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
# aNum = int(a)
# bNum = int(b)
# cNum = int(c)

xp = largestOfThree(a,b,c)

print("The biggest number among the three numbers you have entered is",xp)
