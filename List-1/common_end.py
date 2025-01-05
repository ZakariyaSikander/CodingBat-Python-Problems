# Given 2 arrays of ints, a and b, 
# return True if they have the same first element or they have the same last element.

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]
