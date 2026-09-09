class TrieNode:
    def __init__(self,val="",children=None,eow=False):
        self.val=val
        self.children=set() if not children else children
        self.eow=eow
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        node=self.root
        for char in word:
            # check if char matches any chars under node
            existing=False
            for child in node.children:
                if child.val==char:
                    node=child
                    existing=True
                    break
            if existing:
                continue
            # o.w. create new child
            newChild=TrieNode(val=char)
            node.children.add(newChild)
            node=newChild
        # add eow marker to last node
        node.eow=True
        # check by printing dictionary
        # def dfs(node,i):
        #     for child in node.children:
        #         print(child.val,child.eow)
        #         dfs(child,i+1)
        # dfs(self.root,0)

    def search(self, word: str) -> bool:
        def dfs(node,target,i):
            res = False # for "." case
            char=target[i]
            for child in node.children:
                if child.val==char or char == ".":
                    # reach end
                    if len(target)-1==i:
                        return True if child.eow else False
                    # otherwise keep going
                    # need to find a way to check all routes when "."
                    res = dfs(child,target,i+1) or res
            # dont find in children
            return res
        return dfs(self.root,word,0)  
