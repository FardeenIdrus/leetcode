
class TrieNode:
    def __init__(self):
        self.children = [None] *26
        self.isLeaf = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    # Method to insert a key into the Trie
    # Insertion: O(n), here n is the length of the string inserted
    def insert(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            # Check if the node already exists
            if curr.children[index] is None:
                #If it doesnt exist, create a new node
                curr.children[index] = TrieNode()
            # Move the pointer to the new node
            curr = curr.children[index]
        curr.isLeaf = True

    # Method to search a key in the Trie
    # O(n), here n is the length of the string searched
    def seach(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
        return curr.isLeaf

    #Method to check if a prefix exists in the Trie
    # Prefix searching: Here n is the length of the string searched
    def isPrefix(self, prefix):
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True

if __name__ == '__main__':
    trie = Trie()
    arr = ["and", "ant", "do", "dad"]
    for s in arr:
        trie.insert(s)
    searchKeys = ["do", "gee", "bat"]
    for s in searchKeys:
        if trie.search(s):
            print("true", end= " ")
        else:
            print("false", end=" ")
    
    print()
    prefixKeys = ["ge", "ba", "do", "de"]
    for s in prefixKeys:
        if trie.isPrefix(s):
            print("true", end = " ")
        else:
            print("false", end = " ")