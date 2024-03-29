def valid_brackets(str):
    bracket_map = {"(": ")", "{": "}", "[": "]"}
    opening_bracket = set(["[", "{", "("])

    stack = []

    for i in str:
        if i in opening_bracket:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
            stack.pop()
        else:
            return False

    if stack == []:
        return True
    return False


print(valid_brackets("()["))
print(valid_brackets("([])["))
print(valid_brackets("([])"))
print(valid_brackets("()[]"))
