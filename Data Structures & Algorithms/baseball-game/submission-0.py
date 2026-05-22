class Stack:
    def __init__(self):
        self.scores = []

    def getter(self):
        return self.scores
    
    def push(self, score):
        self.scores.append(score)

    def pop(self):
        if len(self.scores) == 0:
            return None
        return self.scores.pop()

    def peek(self):
        if len(self.scores) == 0:
            return None
        return self.scores[-1]

    def size(self):
        return len(self.scores)

def is_integer(num):
    try:
        int(num)
        return True
    except:
        return False

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = Stack()

        for operation in operations:
            if is_integer(operation):
                stack.push(int(operation))
            elif operation == '+':
                pre_score1 = stack.peek()
                stack.pop()
                pre_score2 = stack.peek()
                new_score = pre_score1 + pre_score2
                stack.push(pre_score1)
                stack.push(new_score)
            elif operation == 'D':
                stack.push(2*stack.peek())
            elif operation == 'C':
                stack.pop()

        return sum(stack.getter())
