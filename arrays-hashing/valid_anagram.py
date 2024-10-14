"""
Valid Anagram Problem
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

"""
from typing import Counter


class Solution:
    def isAnagramOne(self, s: str, t: str) -> bool:
        # First check if the lengths of the two strings are equal. If not, return False immediately.
        if len(s) != len(t):
            return False
        
        # create dictionary to store character and character counts
        countS, countT = {}, {}

        for i in range(len(s)):
            # .get means if the key is not found, it will return 0
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
            
        return True

    # built in Counter class
    def isAnagramTwo(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
    # sorting and direct comparison, less efficient
    def isAnagramThree(self, s: str, t: str) -> bool:
        return (sorted(s) == sorted(t))