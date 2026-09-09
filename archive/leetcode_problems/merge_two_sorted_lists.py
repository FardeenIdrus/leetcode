
from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode()
        current = merged_list
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
            else:
                current.next = list2
                list2 = list2.next
                current = current.next
            
        current.next = list1 or list2 
        return merged_list.next

if __name__ == "__main__":
    sol = Solution()
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)
    list2= ListNode(1)
    list2.next= ListNode(4)
    list2.next.next = ListNode(5)
    print(sol.mergeTwoLists(list1,list2))
            
   