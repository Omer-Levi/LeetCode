class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current_l1, current_l2 = l1, l2
        num_l1, num_l2 = 0, 0
        mod = 1
        new_list = ListNode()
    
        while current_l1:
            num_l1 += (current_l1.val * mod)
            current_l1 = current_l1.next
            mod *= 10
        
        mod = 1
        while current_l2:
            num_l2 += (current_l2.val * mod)
            current_l2 = current_l2.next
            mod *= 10
        sum_list = (num_l1+num_l2)

        head = ListNode(sum_list%10)
        new_list = head
        sum_list //= 10

        while sum_list != 0:
            new_list.next = ListNode(sum_list%10)
            sum_list //= 10
            new_list = new_list.next
        
        return head
    
def main():
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)
    l1.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next.next = ListNode(9)
    
    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)
    

    s = Solution()
    result = s.addTwoNumbers(l1,l2)
    while result:
        print(result.val)
        result = result.next

if __name__ == "__main__":
    main()