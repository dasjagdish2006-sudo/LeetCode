class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        cur = head

        while cur:
            if cur.next and cur.val == cur.next.val:
                duplicate = cur.val

                while cur and cur.val == duplicate:
                    cur = cur.next

                prev.next = cur
            else:
                prev = cur
                cur = cur.next

        return dummy.next