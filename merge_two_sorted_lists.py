# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        head = ListNode(-1)
        current = head
        current1 = list1
        current2 = list2

        while current1 or current2:
            if current1 == None:
                current.next = current2
                break
            elif current2 == None:
                current.next = current1
                break

            if current1.val <= current2.val:
                current.next = ListNode(current1.val)
                current1 = current1.next
            else:
                current.next = ListNode(current2.val)
                current2 = current2.next
            current = current.next
        return head.next


def main():
    l1 = ListNode(2)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    
    s = Solution()
    result = s.mergeTwoLists(l1, l2)
    # print(result)
    while result:
        print(result.val)
        result = result.next

if __name__ == "__main__":
    main()






        
        