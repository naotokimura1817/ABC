N = int(input())
p = list(map(int, input().split()))
q = [x for x in range(0, N)]

for i in range(0, N):
    q[p[i] - 1] = i + 1

print(*q)