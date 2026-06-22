class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans_stack = []
        combined_arr = []
        for p, s in zip(position, speed):
            combined_arr.append((p, s))

        combined_arr.sort(key=lambda x: x[0])

        while combined_arr:
            car = combined_arr.pop()
            time_taken = (target-car[0])/car[1]
            if ans_stack:
                if ans_stack[-1] < time_taken:
                    ans_stack.append(time_taken)
            else:
                ans_stack.append(time_taken)

        return len(ans_stack)
