A = []

with open('text.txt', 'r') as inp:
    for line in inp:
        A.append([str(x) for x in line.split()])
rows = len(A)
maxlen=0
for i in range(0,rows-1):
    words = len(A[i])
    for k in range (0, words-1):
        if (maxlen< len(A[i][k])):
            maxlen= len(A[i][k])
            ryadok=i
            slovo=k
print(A[ryadok][slovo])