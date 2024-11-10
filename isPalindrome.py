# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        current = head
        ls = []

        while current:
            ls.append(current.val)
            current = current.next

        return ls == ls[::-1]

def main():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(1)

    s = Solution()
    result = s.isPalindrome(l1)
    print(result)

if __name__ == "__main__":
    main()