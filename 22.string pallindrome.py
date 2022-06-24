a = str(input("Enter a string : "))

rev = a[::-1]

print("reveresed string : ",rev)

if a == rev:
    print("String is pallindrome")
else:
    print("Not a pallindrome")
