N = 600851475143

def find_factors(number):
  i = 2 
  while i < number:
    if number % i == 0:
      return number/i, i
    i += 1
  return number, 1

def isPrime(number):
  i = 2
  while i < number:
    if number % i == 0:
      return False
    i += 1
  return True

def find_largest_prime_factor(number):
  prime_factors = []
  n = number
  while True:
    p, q = find_factors(n)
    if p != n:
      print p
      print q
      if isPrime(p):
        return p
      if isPrime(q):
        prime_factors.append(p)
      n = p
    else:
      if len(prime_factors) == 0:
        return None
      else:
        return max(prime_factors)
 
#print find_largest_prime_factor(N)
