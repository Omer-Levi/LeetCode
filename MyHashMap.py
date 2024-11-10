class MyHashMap(object):

    def __init__(self):
        self.hashMap = [None]*(1000001)
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hashMap[key] = [key, value]

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.hashMap[key] == None:
            return -1
        return self.hashMap[key][1]
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashMap[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)