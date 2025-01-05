# return true if either integer is 10, or their sum is equal to 10

def makes10(a, b):
  sum = a + b
  return (a == 10 or b == 10) or sum == 10
