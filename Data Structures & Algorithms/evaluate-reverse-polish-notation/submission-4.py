def perform_op(n1, n2, op):
    if op == "*":
        return n1 * n2
    
    if op == "+":
        return n1 + n2
    
    if op == "-":
        return n1 - n2
    
    if op == "/":
        sign = 1
        if (n1 < 0) ^ (n2 < 0):
            sign = -1
        return sign * (abs(n1)//abs(n2))
    return None

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token in "+-*/":
                n = perform_op(st[-2], st[-1], token)
                st.pop()
                st.pop()
                st.append(n)
            else:
                st.append(int(token))
            # print(st)

        return st[-1]