sentence= "alpha coders smvec"

s = sentence.split()[::-1]

l = []

for i in s:
    l.append(i)
print(" ".join(l))