# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        return new_node

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        if head == None:
            return False
        setlist = set()
        while current.next:
            if current in setlist:
                return True
            else:
                setlist.add(current)
        return False
            
        
def main():
    llist = LinkedList()
    llist.insert_at_end(1)
    llist.insert_at_end(2)
    # llist.insert_at_end(0)
    # llist.insert_at_end(-4)
    llist.head
    sol = Solution()
    print(sol.hasCycle(llist.head))
    

if __name__ == "__main__":
    main()