class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 0:
            return ""
        if len(words)==1:
            return words[0]
        # create adj list
        adjList = {}
        for word in words:
            for ch in word:
                adjList.setdefault(ch, set())
        
        prev=words[0]
        for word in words[1:]:
            # compare chars based curr word length:
            prefix=True
            for i in range(min(len(word),len(prev))):
                if prev[i] != word[i]:
                    adjList[prev[i]].add(word[i])
                    prefix=False
                    break
            # invalid case: prefix after
            if prefix and len(prev)>len(word):
                return ""
            # update for next comparison
            prev=word
        print(adjList)
        # go through adjList by topological sort
        def dfs(letter):
            # detect cycle
            if letter in path:
                print("in path")
                return False
            # skip if already seen
            if letter in seen:
                return ""
            seen.add(letter)
            path.add(letter)
            # reached end of graph
            if not adjList[letter]:
                path.remove(letter)
                return letter
            # other wise keep traversing
            res=""
            for nxt in adjList[letter]:
                print(letter,seen)
                out=dfs(nxt)
                if out==False:
                    return False
                res+=out
            res+=letter

            path.remove(letter)
            return res
        # run dfs for all letters
        res=""
        seen=set()
        path=set()
        for letter in adjList:
            out=dfs(letter)
            if out==False:
                return ""
            res+=out
        return res[::-1]
                
            

