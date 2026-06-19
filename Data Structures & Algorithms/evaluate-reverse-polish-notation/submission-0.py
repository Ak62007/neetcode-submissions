class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_stack = []
        
        for token in tokens:
            if token not in ['*', '+', '-', '/']:
                op_stack.append(int(token))
            else:
                sec_dig = op_stack.pop()
                first_dig = op_stack.pop()

                if token == '+':
                    op_stack.append(int(first_dig + sec_dig))
                elif token == '-':
                    op_stack.append(int(first_dig - sec_dig))
                elif token == '*':
                    op_stack.append(int(first_dig * sec_dig))
                else:
                    op_stack.append(int(first_dig / sec_dig))

        return op_stack.pop()

