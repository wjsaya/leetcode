class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lNew = ListNode(0)
        lNow = lNew

        while((l1 is not None) and (l2 is not None)):
            lTemp = ListNode(l1.val + l2.val)
            lNow.next = lTemp
            lNow = lNow.next
            l1 = l1.next
            l2 = l2.next
        
        if (l1 is not None):
            lNow.next = l1
            
        if (l2 is not None):
            lNow.next = l2

        lNew = lNew.next
        lNow = lNew

        while(lNow is not None):
            if(lNow.val > 9):
                if(lNow.next is None):
                    lTemp = ListNode(lNow.val // 10)
                    lNow.next = lTemp
                else:
                    lNow.next.val = lNow.next.val + (lNow.val // 10)
                lNow.val = lNow.val % 10
            lNow = lNow.next
        # return lNew
        doprint(lNew)


def doprint(inList):
    while(inList is not None):
        print(str(inList.val) + "->", end="")
        inList = inList.next

if __name__ == '__main__':
        ln13 = ListNode(3)
        ln12 = ListNode(4)
        ln11 = ListNode(2)
        ln11.next = ln12
        ln12.next = ln13

        ln23 = ListNode(4)
        ln22 = ListNode(6)
        ln21 = ListNode(5)
        ln21.next = ln22
        ln22.next = ln23

        a = Solution()
        a.addTwoNumbers(ln11, ln21)

