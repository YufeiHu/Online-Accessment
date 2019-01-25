


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def initializeLinkedList(input, conn_idx):
    conn_ptr = None
    preHead = ListNode(0)
    ptr = preHead
    for i, val in enumerate(input):
        ptr.next = ListNode(val)
        ptr = ptr.next
        if i == conn_idx:
            conn_ptr = ptr
    ptr.next = conn_ptr
    return preHead.next


class Solution(object):
    def detectCycle(self, head):

        if not head: return None

        p_slow = head
        p_fast = head
        intersection = None
        while p_fast != None and p_fast.next != None:
            if p_fast == p_slow and intersection == None:
                intersection = p_fast
            elif p_fast == p_slow and intersection != None:
                intersection = p_fast
                break
            p_slow = p_slow.next
            p_fast = p_fast.next.next
        if p_fast == None or p_fast.next == None:
            return None

        p1 = head
        p2 = intersection
        while True:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next


input = initializeLinkedList([3], -1)
mySolution = Solution()
ans = mySolution.detectCycle(input)
if ans is not None:
    print(ans.val)
else:
    print(None)