class ListNode:
    def __init__(self,val = 0, next = None) -> None:
        self.val = 0
        self.next = None
    
class solution:
    def mergedList(self,l1, l2):
        newList = ListNode()
        dummy = newList

        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if l1:
            dummy.next = l1
        else:
            dummy.next = l2
        
        return newList.next