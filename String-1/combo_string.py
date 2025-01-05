# Given 2 strings, a and b, return a string of the form short+long+short, 
# with the shorter string on the outside and the longer string on the inside.

def combo_string(a, b):
  return a + b + a if len(a) < len(b) else b + a + b
