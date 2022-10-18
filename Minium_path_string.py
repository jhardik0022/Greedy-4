# Time complexity : O(m*n)
# Space complexity : O(n)
# Leetcode : Solved and submitted

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # make a Hashset of the source string
        pattern = set(source)
        
        # default value of pointers is 0, fine the length and initialize count as 1
        sp = 0
        tp = 0
        sl = len(source)
        tl = len(target)
        count = 1
        
        # traverse over the target string
        while tp < tl:
            # if the char is not in the source string, then return -1
            if target[tp] not in pattern:
                return -1
            
            # if they are equal, then increment both the pointers
            if target[tp] == source[sp]:
                sp += 1
                tp += 1
                
                # check if we have reached to the end of the target string, if so then return the count
                if tp == tl:
                    return count
            else:
                # if not mathcing, then increment the source string
                sp += 1
            
            # if we have reached to the end of the source string, then again start from 0 index and also increment the count
            if sp == sl:
                sp = 0
                count += 1
