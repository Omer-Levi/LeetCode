class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        head_new = ListNode(0)
        current = head
        current_new = head_new

        while current:
            if current.val != val:
                current_new.next = ListNode(current.val)
                current_new = current_new.next
            current = current.next
        return head_new.next


def main():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(6)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next.next = ListNode(6)

    s = Solution()
    result = s.removeElements(l1,6)
    while result:
        print(result.val)
        result = result.next

if __name__ == "__main__":
    main()