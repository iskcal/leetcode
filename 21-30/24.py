def swapPairs(head):
    if head == None or head.next == None:
        return head
    else:
        top = ListNode(0)
        top.next = head
        pre = top # 前一个的前一个
        post = top.next # 后一个的前一个

        while pre.next != None and post.next != None:
            pre.next = post.next
            post.next = post.next.next
            pre.next.next = post
            pre = post
            post = pre.next
        return top.next

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

    t = swapPairs(p11)