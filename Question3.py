n = 600851475143
if n % 2 == 0:
   lastFactor = 2
   n = n / 2
   while n % 2 == 0:
       n = n / 2
else: 
   lastFactor = 1
   factor = 3
   factorMax = n ** 0.5
   while n > 1 and factor <= factorMax:
       while n % factor == 0:
          n = n / factor
       factorMax = n ** 0.5
       factor = factor + 2 
if n == 1:
    print(lastFactor)
else:
    print(n)

        
       
