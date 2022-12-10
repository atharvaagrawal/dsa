def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        k = 0

        for ele in strs[0]:
            flag = 1

            for i in range(len(strs)):
                if (len(strs[i])-1) < k:
                    return res

                if ele != strs[i][k]:
                    flag = 0
                    break
            k += 1

            if flag:
                res += ele
            else:
                break

        return res