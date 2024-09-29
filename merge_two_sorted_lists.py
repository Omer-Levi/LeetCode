# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if l1==None:
        #     return l2
        # if l2==None:
        #     return l1
        # if l1.val>l2.val:
        #     l1,l2=l2,l1
        # head = l1
        # while(l1!=None and l2!=None):
        #     if l1.next==None:
        #         l1.next=l2
        #         return head
        #     if l1.val <= l2.val and l1.next.val>=l2.val:
        #         l2.next,l1.next,l2=l1.next,l2,l2.next
        #     l1=l1.next
        # return head
        stack = []
        current1 = l1
        current2 = l2
        

        while current1 or current2:
            if current1:
                if current1.val <= current2.val:
                    stack.append(current1.val)
                    current1 = current1.next
                else:
                    stack.append(current2.val)
                    current2 = current2.next
            elif current2:
                stack.append(current2.val)
                current2 = current2.next

        return stack


def main():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    
    s = Solution()
    result = s.mergeTwoLists(l1, l2)
    print(result)
    # while result:
    #     print(result.val)
    #     result = result.next

if __name__ == "__main__":
    main()






        
        