#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Author:	wjsaya(http://www.wjsaya.top) 
# @Date:	2018-08-21 23:16:39 
# @Last Modified by:	wjsaya(http://www.wjsaya.top) 
# @Last Modified time:	2018-08-26 09:08:35 
 

# 题目地址:https://leetcode-cn.com/problems/merge-two-sorted-lists/
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # l1,l2任一为空，直接返回另一个
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        # 初始化链表的首位
        if l1.val <= l2.val:
            headre = rspre = ListNode(l1.val)
            l1 = l1.next
        else:
            headre = rspre = ListNode(l2.val)
            l2 = l2.next

        # 遍历l1和l2，对链表赋值
        while(l1 != None and l2 != None):
            temp = ListNode(None)
            if l1.val <= l2.val:
                temp.val = l1.val
                l1 = l1.next
            else:
                temp.val = l2.val
                l2 = l2.next
            headre.next = temp
            headre = headre.next

        # 追加l1与l2剩余部分
        if(l1 != None):
            headre.next = l1
        if(l2 != None):
            headre.next = l2

        return rspre