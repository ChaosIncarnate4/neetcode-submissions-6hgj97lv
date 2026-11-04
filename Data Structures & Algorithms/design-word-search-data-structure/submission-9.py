class WordDictionary:

    def __init__(self):
        self.dict = {}


    def addWord(self, word: str) -> None:
        def helper(word, dict):
            if not word:
                dict['*'] = {}
                return
            
            letter = word[0]

            if letter not in dict:
                dict[letter] = {}
            
            helper(word[1:], dict[letter])
        
        helper(word, self.dict)


    def search(self, word: str) -> bool:
        word += '*'

        def helper(word, dict):
            if word == '*':
                return word in dict
            
            letter = word[0]
            
            if letter == '.':
                for k in dict.keys():
                    if helper(word[1:], dict[k]) == True:
                        return True
                return False
            
            if letter not in dict:
                return False
            
            return helper(word[1:], dict[letter])

        return helper(word, self.dict)
