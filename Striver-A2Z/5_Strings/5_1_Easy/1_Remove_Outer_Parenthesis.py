def removeOuterParentheses(self, s: str) -> str:
        # (())() -> (()) ()
        # (()(())) -> ( () (()) )
        # (()())(()) ->(()()) (()) -> ()() ()
        # (()())(())(()(())) ->(()()) (()) (()(())) -> ()()  () () (())
        
        answer = []
        stack = []
        
        for x in s:
            if x == "(":
                if stack:
                    answer.append("(")
                stack.append("(")
            elif x == ")":
                stack.pop()
                if stack:
                    answer.append(")")
        
        return "".join(answer)
        
        # result = []
        # counter = 1
        # i = 1
        # while i < len(s):

        #     counter += 1 if s[i] == "(" else -1
            
        #     if counter != 0:
        #         result.append(s[i])
        #     else: # counter = 0
        #         counter = 1 # Found '('
        #         i += 1
            
        #     i += 1

        # return "".join(result)