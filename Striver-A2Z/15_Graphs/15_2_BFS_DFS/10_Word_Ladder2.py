
from queue import Queue

# TLE
""" class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        # We will use flag = 0-not found ,1-found, 2-waiting for level to check
        res = []

        a_z = [chr(i) for i in range(97, 123)]

        q = Queue()
        q.put([beginWord, [beginWord]])

        s = set(wordList)

        if beginWord in s:
            s.remove(beginWord)

        flag = 0

        # print("Word:",wordList)

        while q.qsize():

            word, tmp = q.get()

            # print(word,len(tmp),flag)

            if flag != 0 and flag < len(tmp):
                break

            if word == endWord:
                res.append(tmp)
                flag = len(tmp)

            for i in range(len(word)):

                word_ch = [c for c in word]

                for ch in a_z:
                    word_ch[i] = ch
                    word_ = ''.join(word_ch)

                    if word_ in tmp:
                        continue

                    if word_ in s:
                        t = tmp.copy()
                        t.append(word_)
                        q.put([word_, t])

        return res
"""
