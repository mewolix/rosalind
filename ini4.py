a, b = map(int, input().split())
a = a + 1 if a % 2 else a
b = b - 1 if b % 2 else b
print((a + b) * (b - a) // 4)
