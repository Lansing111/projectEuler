m = 20
n = 1 
i = 1
check = 1
largest = m ** 0.5
p = [2,3,5,7,11,13,17,19]
a = [4,2,1,1,1,1,1,1,1]
while p[i] <= m:
      a[i] = 1
      if check == 1:
          if p[i] <= largest:
               a[i] = log(k)//log(p[i])
          else: 
               check = 0
      n = n * p[i] ** a[i]
      i = i + 1
print(N)
      
            
      