a = 1
d = 4
terms = 20
series = []

for i in range(terms):
    series.append(a)
    a += d

for term in series:
    print(term, end=" ") 