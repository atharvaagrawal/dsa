class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0

        short1 = 0
        short2 = 0


        i = startIndex
        n = len(words)

        while True:
            if words[i] == target:
                break
            i = (i + 1) % n
            short1 += 1
            if short1 == n:
                return -1
                
        i = startIndex
        while True:
            if words[i] == target:
                break
            i = (i - 1) % n
            short2 += 1
            if short2 == n:
                return -1
        return min(short2,short1)