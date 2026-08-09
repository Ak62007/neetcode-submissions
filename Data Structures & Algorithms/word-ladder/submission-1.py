class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def check(w1, w2) -> bool:
            if len(w1) != len(w2):
                return False
            n = len(w1)
            count = 0
            for i in range(n):
                if w1[i] != w2[i]:
                    count += 1

            if count != 1:
                return False
            else:
                return True

        adj = defaultdict(list)
        c_word_list = list(set([beginWord] + wordList))
        for i in range(len(c_word_list)):
            for j in range(len(c_word_list)):
                if i == j:
                    continue
                if check(c_word_list[i], c_word_list[j]):
                    adj[c_word_list[i]].append(c_word_list[j])

        if not adj:
            return 0
        # print(adj)
        # def bfs(w):
        #     visit = set()
        #     q = deque()
        #     q.append(w)
        #     path_length = 0
        #     min_path = len(wordList) + 1
        #     while q:
        #         print("queue state: \n", q)
        #         print("visit state: \n", visit)
        #         word = q.popleft()
        #         visit.add(word)
        #         path_length += 1

        #         for nei in adj[word]:
        #             if nei in visit:
        #                 continue
        #             if nei == endWord:
        #                 if path_length < min_path:
        #                     min_path = path_length
        #                 return min_path

        #             q.append(nei)

        #         # visit.remove(word)

        #     return 0

        min_path = len(wordList) + 2
        visit = set()
        def dfs(w, path_len: int):
            nonlocal min_path
            if w == endWord:
                if path_len < min_path:
                    min_path = path_len
                    return

            if w not in visit:
                visit.add(w)

            for word in adj[w]:
                if word in visit:
                    continue
                dfs(word, path_len+1)

            visit.remove(w)


        dfs(beginWord, 1)

        if min_path == len(wordList) + 2:
            return 0
        else:
            return min_path