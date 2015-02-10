def reverse ( m ):
  reverse = 0
  while m > 0:
    reverse = m % 10 + 10 * reverse
    m = (m - m % 10) / 10
    
def Palindrome( m ):
    m = reverse( m )
    return m
largestPalin = 0
a = 100
while a <= 999:
      b = 100
      while b <= 999:
          if Palindrome(a) == b and (a*1000 + b) > largestPalin:
              largestPalin = a*1000 + b
          b = b + 1
a = a + 1
print(largestPalin)
        
