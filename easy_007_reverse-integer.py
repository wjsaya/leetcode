#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Author:	wjsaya(http://www.wjsaya.top) 
# @Date:	2018-08-19 12:24:16 
# @Last Modified by:	wjsaya(http://www.wjsaya.top) 
# @Last Modified time:	2018-08-19 16:05:29 
 
 
# 题目地址:https://leetcode-cn.com/problems/reverse-integer
# 给定一个 32 位有符号整数，将整数中的数字进行反转。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
# 示例 1:

# 输入: 123
# 输出: 321

#  示例 2:

# 输入: -123
# 输出: -321

# 示例 3:

# 输入: 120
# 输出: 21

class Solution:
    def reverse(self, x):
        """
        1. 数字转数组
        2. 数组reverse
        3. 数组转数字
        """
        tag = 1 if x > 0 else -1
        x = x * tag

        a = []
        for i in str(x):
            a.append(i)
        a.reverse()
        resp = ''.join(a)
        resp = int(resp)

        if (resp > pow(2, 31)-1) or (resp < -pow(2, 31)):
            return 0
        return resp * tag

    def reverse2(self, x):
        tag = 1 if x > 0 else -1
        x = x * tag
        # tag用来转换正负
        rev = 0
        
        while(x != 0):
            pop = x % 10
            x = int(x / 10)
            # 取出第一位数字到pop，然后删掉原数字
            rev = rev * 10 + pop
            # ((返回数*10)+取出的第一位数)
            # 这样就在返回数的尾巴上加上了原数字的第一个数

        if (rev > pow(2, 31)-1) or (rev < -pow(2, 31)):
            # 如果结果超出范围，返回0
            return 0
        return rev*tag
        # 转换正负
    

test = Solution()
print(test.reverse(-12345))