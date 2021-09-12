P = list(map(int, input().split()))

s = 'abcdefghijklmnopqrstuvwxyz'
S = ''

for i in range(0, len(P)):
    S += s[P[i] - 1]

print(S)
