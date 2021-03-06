# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1list = []
        l2list = []
        l1lis = []
        l2lis = []
        while l1 != None:
            print(l1.val)
            l1list.append(l1.val)
            l1 = l1.next
        while l2 != None:
            print(l2.val)
            l2list.append(l2.val)
            l2 = l2.next
        l1lis = [str(i) for i in l1list]
        l2lis = [str(i) for i in l2list]
        
        l1lis = ''.join(l1lis)
        l2lis = ''.join(l2lis)
        l1lis = int(l1lis)
        l2lis = int(l2lis)
        l3 = l1lis + l2lis
        l4 = str(l3)
        print(l4)
        l5 = list(l4)
        l6 = [int(i) for i in l5]
        print("hi")
        print(l6)
        
        head = None
        tail = None
        for i in range(len(l6)):
            node = ListNode(l6[i],None)
            if (head == None):
                head = node
                tail = node
            else:    
                tail.next =node
                tail = node
        print(head)
        return head