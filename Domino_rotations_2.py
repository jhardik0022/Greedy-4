# Time complexity : O(n)
# Space complexity : O(1)
# Leetcode : Solved and submitted

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # call the check function with the first element of tops
        res = self.check(tops, bottoms, tops[0])
        # If no result was found, then call on the first elements of bottoms
        if res != -1:
            return res
        return self.check(tops, bottoms, bottoms[0])
    
    # check for the ele in tops and bottoms for possible result
    def check(self, tops, bottoms, ele):
        
        # default values for rotations
        rT = rB = 0
        
        # traverse over the array
        for i in range(len(tops)):
            # if none of the elements from top and bottom are equal to ele, then return -1
            if tops[i] != ele and bottoms[i] != ele:
                return -1
            
            # if the element in top is not equal to ele, increment the rotation of tops
            elif tops[i] != ele:
                rT += 1
            
            # if the element in bottom is not equal to ele, increment the rotation of bottoms
            elif bottoms[i] != ele:
                rB += 1
        
        # return the minimum of both the rotations
        return min(rT, rB)
