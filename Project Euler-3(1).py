n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n /i
    i = i + 1
if n == 1:
    print(i-1)
else:
    print(n)   