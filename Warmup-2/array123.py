# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
  return [1, 2, 3] in [nums[i : i + 3] for i in range(len(nums) - 2)]
