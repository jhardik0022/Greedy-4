# Time complexity : O(2*n)
# Space complexity : O(1)
# Leetcode : Solved and submitted

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # define a hashmap, and default candidate which could be a probable solution
        domino = {}
        n = len(tops)
        cand = -1
        
        # fill the hashmap with the frequency of the number
        # candidate is anyone which occurs more than the half number of times
        for i in range(n):
            t = tops[i]
            b = bottoms[i]
            
            if t not in domino:
                domino[t] = 0
            domino[t] += 1
            if domino[t] >= n:
                cand = t
                break
            
            if b not in domino:
                domino[b] = 0
            domino[b] += 1
            if domino[b] >= n:
                cand = b
                break
        
        # if none of the numbers occured more than half times, return -1
        # as we cannot reach the result
        if cand == -1:
            return cand
        
        # Default values for rotations of tops and bottoms array
        rotT = rotB = 0
        
        # traverse over the array
        for i in range(n):
            # if none of the array at that index has the candidate, then return -1
            if tops[i] != cand and bottoms[i] != cand:
                return -1
            # if the tops element at index doesn not cand, increment the rotation
            elif tops[i] != cand:
                rotT += 1
            # if the bottoms element at index doesn not cand, increment the rotation
            elif bottoms[i] != cand:
                rotB += 1
        
        # result is the minimum of both the rotations
        return min(rotT, rotB)
