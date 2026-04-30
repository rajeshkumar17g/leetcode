class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        prev=head
        crr=head.next
        while crr!=None:
            if prev.val==crr.val:
                prev.next=crr.next
                crr=crr.next
            else:
                prev=prev.next
                crr=crr.next
        return head