def removeNthFromEnd(head, n):
        if not head:
            return None
        else:
            p1 = head
            p2 = head
            for i in range(n-1):
                if not p1.next:
                    return None
                else:
                    p1 = p1.next
            if not p1.next:
                return head.next
            else:
                p1 = p1.next
                while p1.next:
                    p1 = p1.next
                    p2 = p2.next
                p2.next = p2.next.next if p2.next != None else None
                return head


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    p1 = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    p5 = ListNode(5)

    head = p1
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = None

    head_m = removeNthFromEnd(head, 2)

    p = head_m
    while not p.next:
        print(p.val)