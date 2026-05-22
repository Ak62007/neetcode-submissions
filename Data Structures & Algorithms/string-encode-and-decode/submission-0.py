class Solution:
    def __init__(self):
        self.lengths = []
        
    def encode(self, strs: List[str]) -> str:
        cs = ""
        for s in strs:
            cs = cs + s
            self.lengths.append(len(s))
        return cs
    def decode(self, s: str) -> List[str]:
        index = 0
        final_ans = []
        for l in self.lengths:
            final_ans.append(s[index:index + l])
            index += l
        return final_ans