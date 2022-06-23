number = [23, 23, 3232, 2, 32, 3]
print(number)
print(number[2])
number.append(26)
print(number)

number.insert(0, 33)  # INSERTS THE NUMBER IN THE LIST IN THE GIVEN INDEX
print(number)
print("length of the list ", len(number))

print(number.pop())  # REMOVES AND RETURNS THE LAST VALUE IN THE STRING
print(number)

number.remove(3232)  # REMOVES THE GIVEN NUMBER FROM THE LIST
print(number)

List = []
print("INITIAL BLANK LIST")
print(List)

# ADDITON OF ELEMENTS
List.append(1)
List.append(2)
List.append(4)

print("\nlist after addition of three elements : ")
print(List)

# ADDING ELEMENTS TO THE LIST USING ITERATOR

for i in range(1, 4):
    List.append(i)
print("\n List after addition of elements from 1-3")
print(List)

# ADDING TUPLES TO THE LIST
List.append((5, 6))
print("List after addition of tuple ")
print(List)

# ADDITION OF LIST TO A LIST
List2 = ['for', 'geeks']
List.append(List2)
print("\n List after addition of a list ")
print(List)
print(List[6])
List3 = []

for i in range(1, 21):
    if (i % 2 == 0):
        List3.append(i ** 2)

print(List3)

#LIST COMPREHENSION

List4 = [i**2 for i in range(1,21) if(i%2==0)]
print(List4)