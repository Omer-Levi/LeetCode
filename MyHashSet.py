class MyHashSet(object):

    def __init__(self):
        self.hashSet = [None]*1000001
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashSet[key] = key

        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashSet[key] = None
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if self.hashSet[key] == key:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)