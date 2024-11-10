# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        current = head
        number_nodes = -1
        decimal_value = 0

        while current:
            number_nodes += 1
            current = current.next
        current = head

        while number_nodes >= 0:
            if current.val == 1:
                decimal_value += (2 ** number_nodes)
            current = current.next
            number_nodes -= 1
        return decimal_value
            
def main():
    l1 = ListNode(1)
    l1.next = ListNode(0)
    l1.next.next = ListNode(1)

    s = Solution()
    result = s.getDecimalValue(l1)
    print(result)

if __name__ == "__main__":
    main()