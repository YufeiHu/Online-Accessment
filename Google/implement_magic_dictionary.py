from collections import defaultdict


class TrieNode(object):

    def __init__(self):
        self.path = defaultdict(TrieNode)
        self.flagWord = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        trie = self.root
        for c in word:
            trie = trie.path[c]
        trie.flagWord = True


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def buildDict(self, words):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in words:
            self.trie.addWord(word)

    def DFS(self, word, idx, flagDiff, trie):

        if flagDiff >= 2: return False
        if idx == len(word) - 1:
            if flagDiff == 0:
                for c in trie.path:
                    if c != word[idx] and trie.path[word[idx]].flagWord:
                        return True
                return False
            else:
                for c in trie.path:
                    if c == word[idx] and trie.path[word[idx]].flagWord:
                        return True
                return False

        for cNew in trie.path.keys():
            print(cNew)
            if word[idx] != cNew and self.DFS(word, idx + 1, flagDiff + 1, trie.path[cNew]):
                return True
            if word[idx] == cNew and self.DFS(word, idx + 1, flagDiff, trie.path[cNew]):
                print("fuck1")
                return True

        return False

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return self.DFS(word, 0, 0, self.trie.root)



myDict = MagicDictionary()
myDict.buildDict(["hello","hallo","leetcode"])
print(myDict.search("hell"))