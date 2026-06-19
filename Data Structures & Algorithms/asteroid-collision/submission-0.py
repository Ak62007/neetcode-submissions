from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans_stack = deque()
        while asteroids:
            if not ans_stack:
                ans_stack.appendleft(asteroids.pop())
            else:
                sec_lst_ast = asteroids.pop()
                lst_ast = ans_stack[0]
                crash = (sec_lst_ast > 0) and (lst_ast < 0)

                if crash:
                    if abs(sec_lst_ast) > abs(lst_ast):
                        ans_stack.popleft()
                        ok = False
                        while not ok:
                            if ans_stack:
                                lst_ast = ans_stack[0]
                                crash = (sec_lst_ast > 0) and (lst_ast < 0)
                                if crash:
                                    if abs(sec_lst_ast) > abs(lst_ast):
                                        ans_stack.popleft()
                                    elif abs(sec_lst_ast) == abs(lst_ast):
                                        ans_stack.popleft()
                                        ok = True
                                    else:
                                        ok = True
                                else:
                                    ans_stack.appendleft(sec_lst_ast)
                                    ok = True
                            else:
                                ans_stack.appendleft(sec_lst_ast)
                                ok = True
                    elif abs(sec_lst_ast) == abs(lst_ast):
                        ans_stack.popleft()
                else:
                    ans_stack.appendleft(sec_lst_ast)

        return list(ans_stack)
