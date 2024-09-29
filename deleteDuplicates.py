# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ls = ListNode()
        ls.val = head.val
        current = head
    
        while current.next:
            if current.val != ls.val:
                ls.next = ListNode(current.val)
                ls = ls.next
            current = current.next
        return ls


def main():
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(3)
    l1.next.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next.next = ListNode(4)
    

    s = Solution()
    result = s.deleteDuplicates(l1)
    while result:
        print(result.val)
        result = result.next

if __name__ == "__main__":
    main()