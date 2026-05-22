class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def create_initial_map(word: str) -> dict:
            initial_dic = {}
            set_str = set(word)
        
            for key in list(set_str):
                initial_dic[key] = 0
            
            return initial_dic

        def create_map(string: str, key_map: dict) -> dict:
            hashset = set()
            for letter in string:
                if letter in hashset:
                    key_map[letter] += 1
                else:
                    hashset.add(letter)
            return key_map

        def compare(a: dict, b: dict) -> bool:
            key_a = set(a.keys())
            key_b = set(b.keys())
            if not key_a == key_b:
                return False
            else: 
                for key in key_a:
                    if not a[key] == b[key]:
                        return False
                return True

        i_s = create_initial_map(s)
        i_t = create_initial_map(t)

        map_s = create_map(s, i_s)
        map_t = create_map(t, i_t)

        return compare(map_s, map_t)