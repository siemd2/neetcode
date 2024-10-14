"""
Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""

# There are multiple ways to solve this problem. In order from worst to best time complexity:
# 1. Brute force: Compare each element with all other elements in the array. Time complexity: O(n^2)
# 2. Sorting: Sort the array and then compare adjacent elements. Time complexity: O(nlogn)
# 3. Hashset: Use a hashset to store the elements and check if the element is already present in the hashset. Time complexity: O(n)

# We will use the hashset approach to solve this problem.

class solution:
    def containsDuplicate(self, nums):
        # init hashset to store nums
        hashset = set()
        # iterate through nums
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
    

# test solution
s = solution()
print(s.containsDuplicate([1, 2, 3, 4, 4])) # True