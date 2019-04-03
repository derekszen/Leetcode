class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hammingDist: int = 0 
        xorResult = x ^ y
        while xorResult != 0:
            if(xorResult & 0x1):
                hammingDist += 1
            xorResult = xorResult >> 1
            
        return hammingDist