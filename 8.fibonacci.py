#program for fibonacci series
limit = (int(input("Enter the limit ")))
n1  = 0
n2 = 1
n3 = 0
print(n1)
print(n2)

for i in range(2,limit):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print( n3 )
    