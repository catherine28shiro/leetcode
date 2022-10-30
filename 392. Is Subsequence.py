"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""
"""
Input: s = "abc", t = "ahbgdc"
Output: true
"""


class Solution:
    #solution 1, good one, count the number of s characters in t
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        for c in t:
            if count < len(s):
                if s[count] == c:
                    count += 1

        return count == len(s)

    #solution 2, slow one
    def isSubsequence2(self, s: str, t: str) -> bool:
        arr=[]
        t_copy= t
        for i in range(len(s)):
            if s[i] not in t_copy:
                return False
            p = t_copy.index(s[i])
            arr.append(p)
            t_copy=t_copy[p+1:]
            print(t_copy)
            print(arr)
        return True
        

def main():
    sol = Solution()    
    s="aaaaaa"
    t="bbaaaa"

    print(sol.isSubsequence(s,t)) 
    

if __name__ == "__main__":
    main()