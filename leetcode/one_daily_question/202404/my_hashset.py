class MyHashSet(object):

    def __init__(self):
        """
        init
        """
        self.length = 798
        self.table = [[] for _ in range(self.length)]
    
    def hash(self, key):
        """
        hash
        """
        return key % self.length

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.contains(key):
            hash_key = self.hash(key)
            self.table[hash_key].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            hash_key = self.hash(key)
            self.table[hash_key].remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        hash_key = self.hash(key)
        for v in self.table[hash_key]:
            if v == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)