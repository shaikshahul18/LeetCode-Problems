class ListNode:
    def __init__(self,val = 0, next = None) -> None:
        self.val = val
        self.next = next
class solution:
    def reverseList(self,head):
        if not head:
            return
        curr = head
        prev = None
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def reverseLLRecursive(self,head):
        if not head:
            return
        newHead = head
        if head.next:
            newHead = self.reverseLLRecursive(head.next)
            head.next.next = head
        head.next = None

        return newHead

