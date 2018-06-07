def reverseKGroup(head, k):
    if head == None or k == 1:
        return head
    top = ListNode(0)
    top.next = head
    head = top
    tail = top
    p = tail.next
    while head != None and p != None:
        i = 2
        head = tail
        tail = p
        head.next = tail
        p = p.next
        if check(tail, k):
            while i <= k and p != None:
                c = p
                p = p.next
                c.next = head.next
                head.next = c
                i += 1
        else:
            while tail.next != None:
                tail = tail.next
            break
    tail.next = None
    return top.next

def check(p, k):
    i = 0
    while p != None:
        i += 1
        p = p.next
        if i == k:
            break
    if i == k:
        return True
    else:
        return False

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    p11 = ListNode(1)
    p12 = ListNode(2)
    p13 = ListNode(3)
    p14 = ListNode(4)

    p11.next = p12
    p12.next = p13
    p13.next = p14
    p14.next = None

    t = reverseKGroup(p11, 2)