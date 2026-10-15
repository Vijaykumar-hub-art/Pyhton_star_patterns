##this is for right angled triangle

n = 5
for i in range(1, n + 1):
    print("* " * i)


##this is for inverted triangle

n = 5
for i in range(n, 0, -1):
    print("* " * i)


##this is for left alinged triangle

n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

##for pyramid

  n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

##for inverted pyramiid

n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)

##for diamond

n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

##for hollow square

n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

##for hollow triangle

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

##for hour glass

n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)
for i in range(2, n + 1):
    print(" " * (n - i) + "* " * i)

##for x pattern

n = 7
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
