class PrefixTree:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        word += '*'

        def helper(dict, word):
            if not word:
                return
            else:
                letter = word[0]
                if letter not in dict:
                    dict[letter] = {}
                helper(dict[letter], word[1:])

        helper(self.tree, word)

    def search(self, word: str) -> bool:
        word += '*'

        def helper(dict, word):
            if not word:
                return True
            else:
                letter = word[0]
                if letter not in dict:
                    return False
                return helper(dict[letter], word[1:])
        
        return helper(self.tree, word)

    def startsWith(self, prefix: str) -> bool:
        def helper(dict, word):
            if not word:
                return True
            else:
                letter = word[0]
                if letter not in dict:
                    return False
                return helper(dict[letter], word[1:])
        
        return helper(self.tree, prefix)
        