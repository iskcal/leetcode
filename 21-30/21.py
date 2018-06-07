def mergeTwoLists(l1, l2):
    if l1 == None and l2 == None:
        return None
    p1 = l1
    p2 = l2
    head = ListNode(0) # 头节点
    p = head
    while p1 != None and p2 != None:
        if p1.val <= p2.val:
            p.next = p1
            p1 = p1.next
        else:
            p.next = p2
            p2 = p2.next
        p = p.next

    if p1 == None:
        p.next = p2
    else:
        p.next = p1
        
    return head.next

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    p11 = ListNode(1)
    p12 = ListNode(2)
    p13 = ListNode(4)

    p11.next = p12
    p12.next = p13
    p13.next = None

    p21 = ListNode(1)
    p22 = ListNode(3)
    p23 = ListNode(4)

    p21.next = p22
    p22.next = p23
    p23.next = None

    t = mergeTwoLists(None, p21)