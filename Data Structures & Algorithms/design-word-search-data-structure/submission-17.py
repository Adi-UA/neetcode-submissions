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
        def dfs(node,j):
            # basic idea: go down the word for perfect matches
            # only use dfs when encountering a "."
            for i in range(j,len(word)):
                c=word[i]
                if c == ".":
                    for child in node.children.values(): # child nodes
                        if dfs(child,i+1):
                            return True
                    return False # didn't find match
                elif c in node.children:
                    node=node.children[c]
                else:
                    return False
            return node.eow
        return dfs(self.root,0)  
