def maximumValue(self, strs: List[str]) -> int:
    m = 0
    for i in range(len(strs)):
        if strs[i].isnumeric():
            m = max(m,int(strs[i]))
        else:
            m = max(m,len(strs[i]))
    return m
