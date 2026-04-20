class Solution:
    def encode(self, strs: List[str]) -> str:
        # return None if no string
        if len(strs) == 0:
            return "empty"
        # return a joined STRING by spaces
        return ".".join(strs)

    def decode(self, s: str) -> List[str]:
        # return LIST that is empty if input string is empty
        if s == 'empty':
            return []

        # return LIST which separated the string input by spaces
        # cannot return list if nothing to separate
        return s.split(".")


# [] ->  "" -> []
# [""] ->  "" -> [""] 
