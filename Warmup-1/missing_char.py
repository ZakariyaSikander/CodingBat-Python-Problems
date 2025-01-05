# Given a non-empty string and an int n, return a new string where the char at index n has been removed.

def missing_char(str, n):
  return str[:n] + str[n + 1:]
