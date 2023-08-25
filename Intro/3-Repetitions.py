dna = input()

l = 0
r = 0
res = 0
for i in range(1, len(dna)):
    if dna[l] == dna[i]:
        r = i
        res = max(r-l, res)
    else:
        l = i


print(res + 1)