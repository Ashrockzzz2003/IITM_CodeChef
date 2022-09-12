n = int(input())

# 1 + 2 + 3 = 6
# n should leave remainder 0 or 1 or 3 when divided by 6 to reach that point a

if (n % 6 == 0) or (n % 6 == 1) or (n % 6 == 3):
    print("yes")
else:
    print("no")
