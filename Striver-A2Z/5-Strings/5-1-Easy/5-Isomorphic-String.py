def isIsomorphic(self, s: str, t: str) -> bool:
        # Creating a dict which will map 
        # the char 

        d = dict()

        for i in range(len(s)):
            if s[i] in d.keys():
                if d[s[i]] != t[i]:
                    return False
            else:
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
        
        return True