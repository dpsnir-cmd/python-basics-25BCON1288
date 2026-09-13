n = 8
a = 0
b = 1

print("Fibonacci Series:", end=" ")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()