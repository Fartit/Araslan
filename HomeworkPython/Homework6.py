s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
result = []

for i in range(len(s)):
    a = False
    for j in range(len(s)):
        if i != j and s[i] == s[j]:
            a = True
            break
    if not a:
        result.append(s[i])

for d in result:
    print(d, end=' ')











