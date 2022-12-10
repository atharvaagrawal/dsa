def largestOddNumber(self, num: str) -> str:
        # TLE   
        # for i in range(len(num),-1,-1):
        #     if int(num)%2 != 0:
        #         return num
        #     num = num[:i]

        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 != 0:
                return num[:i+1]

        return "" 