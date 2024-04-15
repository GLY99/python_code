base = 789

class MyHashMap(object):

    def __init__(self):
        """
        init
        """
        self.data = [[] for _ in range(base)]

    def hash(self, key):
        """
        hash
        """
        return key % base
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_key = self.hash(key)
        for e in self.data[hash_key]:
            if e.keys()[0] == key:
                e[key] = value
                return
        self.data[hash_key].append({key: value})

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hash_key = self.hash(key)
        for e in self.data[hash_key]:
            if e.keys()[0] == key:
                return e[key]
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_key = self.hash(key)
        for e in self.data[hash_key]:
            if e.keys()[0] == key:
                self.data[hash_key].remove(e)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)