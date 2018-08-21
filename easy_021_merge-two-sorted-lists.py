#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Project: PROJECTNAME(PROJECTURL) 
# @Author:	wjsaya(http://www.wjsaya.top) 
# @Date:	2018-08-21 23:16:39 
# @Last Modified by:	wjsaya(http://www.wjsaya.top) 
# @Last Modified time:	2018-08-21 23:16:39 
 

# 题目地址:https://leetcode-cn.com/problems/merge-two-sorted-lists/
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = [int(i) for i in l1.split("->")]
        l2 = [int(i) for i in l2.split("->")]
        
        if len(l1) == 0:
            return l2
        if len(l2) == 0:
            return l1
            
        lr = []
        l1head = l1.pop(0)
        l2head = l2.pop(0)
            
        while(len(l1) != 0 and len(l2) != 0):
            # print("loop on\t\t|", l1head, l2head, l1, l2, lr)
            # print(l1head, "?????", l2head)
            if l1head <= l2head:
                lr.append(l1head)
                l1head = l1.pop(0)
            else:
                lr.append(l2head)
                l2head = l2.pop(0)
            # print("loop off\t|", l1head, l2head, l1, l2, lr)
            # print(l1head, l2head)
            # print(l1, l2)

        print("loop off\t|", l1head, l2head, l1, l2, lr)
        
        while len(l1) != 0:
            l1head = l1.pop(0)
            lr.append(l1head)
            
        while len(l2) != 0:
            l2head = l2.pop(0)
            lr.append(l1head)
        
        print("loop off\t|", l1head, l2head, l1, l2, lr)
        


# l1 = "1->2->4"
# l2 = "1->3->4"
l1 = "1->2->3"
l2 = "10->20->30"
test = Solution()
print(test.mergeTwoLists(l1, l2))  

