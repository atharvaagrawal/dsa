from queue import Queue


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # Travese from 'a' to 'z'
        # Check if it is present in wordlist

        a_z = [chr(i) for i in range(97, 123)]

        queue = Queue()

        # BFS traversal with pushing values in queue
        # when after a transformation, a word is found in wordList.
        queue.put([beginWord, 1])

        # Push all values of wordList into a set
        # to make deletion from it easier and in less time complexity.
        s = set(wordList)

        if beginWord in s:
            s.remove(beginWord)

        while queue.qsize():
            word, step = queue.get()

            if word == endWord:
                return step

            # Now, replace each character of ‘word’ with char
            # from a-z then check if ‘word’ exists in wordList.
            for i in range(len(word)):
                word_check = [j for j in word]
                for ch in a_z:

                    word_check[i] = ch

                    # check if it exists in the set and push it in the queue.
                    if ''.join(word_check) in s:
                        queue.put([''.join(word_check), step+1])
                        s.remove(''.join(word_check))

        # If there is no transformation sequence possible
        return 0
