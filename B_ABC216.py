n = int(input())

names = []

for _ in range(0, n):
    row = list(map(str, input().split()))
    names.append(row)

flag = False

for i in range(0, n-1):
    for j in range(i+1, n):
        if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
            flag = True

if flag:
    print("Yes")
else:
    print("No")