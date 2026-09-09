class TrieNode:
    def __init__(self,children=None,eow=False):
        self.children={} if not children else children
        self.eow=eow
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        node=self.root
        for char in word:
            # check if char matches any chars under node
            node.children[char]=node.children.get(char,TrieNode())
            node = node.children[char]
        # add eow marker to last node
        node.eow=True

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i == len(word):
                return node.eow
            c=word[i]
            # search all options for wildcard match
            if c == ".":
                for child in node.children.values():
                    if dfs(child,i+1):
                        return True
            # perfect match
            elif c in node.children:
                child=node.children[c]
                return dfs(child,i+1)
            # dont find in children
            return False
        return dfs(self.root,0)  
