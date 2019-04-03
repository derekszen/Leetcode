class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum([1 if c in set(J) else 0 for c in S])