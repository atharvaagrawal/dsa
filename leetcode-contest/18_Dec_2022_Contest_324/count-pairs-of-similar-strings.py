class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        l = []
        ans = 0
        
        for i in range(len(words)):
            d = dict()
            for j in words[i]:
                d[j] = 0
            l.append(d)
        
        # print(l)
        
        for i in range(len(l)):    
            for j in range(i+1,len(l)):
                if l[i] == l[j]:
                    ans +=1
            
                
        return ans