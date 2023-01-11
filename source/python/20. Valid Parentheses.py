class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        if len(s) % 2 != 0:
            return False

        stack: list[str] = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                if c == ")":
                    if stack.pop() != "(":
                        return False
                elif c == "]":
                    if stack.pop() != "[":
                        return False
                elif c == "}":
                    if stack.pop() != "{":
                        return False

        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()

    assert s.isValid("()") == True
    assert s.isValid("()[]{}") == True
    assert s.isValid("(]") == False
    assert s.isValid("([)]") == False
    assert s.isValid("{[]}") == True

    print("All tests passed!")
