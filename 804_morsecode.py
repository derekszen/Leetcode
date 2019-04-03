class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alp_b_l =  [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        resultset: set[str] = set()
        for word in words:
            resultset.add("".join([alp_b_l[ord(c)-97] for c in word]))
        return len(resultset)