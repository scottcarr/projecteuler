first = 1
second = 2
sum = 2 # the second term is even

while second <= 4000000:
  tmp = first + second
  first = second
  second = tmp
  if tmp % 2 == 0:
    sum += tmp

print sum
