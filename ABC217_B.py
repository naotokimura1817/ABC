S = ['ABC', 'ARC', 'AGC', 'AHC']

a = input()
b = input()
c = input()

S.remove(a)
S.remove(b)
S.remove(c)

print(*S)