a = str(input())

i, f = a.split(".")
y = int(f)

if 0 <= y and y <=2:
    print(str(i) + "-")
elif 3 <= y and y <=6:
    print(i)
else:
    print(str(i) + "+")