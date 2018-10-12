#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Author:	wjsaya(http://www.wjsaya.top) 
# @Date:	2018-08-19 16:06:03 
# @Last Modified by:	wjsaya(http://www.wjsaya.top) 
# @Last Modified time:	2018-08-19 17:07:06 
 

# 题目地址:https://leetcode-cn.com/problems/palindrome-number/description/
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 输入: 121
# 输出: true

# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。

class Solution:
    def isPalindrome1(self, x):
        """
        最初的想法。。。
        """
        lis = []
        for i in str(x):
            lis.append(i)
        for i in range(int(len(lis) / 2)):
            if lis[i] != lis[len(lis) - 1 - i]:
                return False
            else:
                continue
        return True

    def isPalindrome2(self, x):
        '''
        负数直接false \n
        正数直接转为字符串然后反序与原数字比较 \n
        '''
        if x < 0:
            return False
        else:
            return str(x)[::-1] == str(x)

    def isPalindrome(self, x):
        '''
        不转成字符串，直接比较
        '''
        if ((x < 0) or (x % 10 == 0 and x !=0)):
            # 负数，以及1-9，均为false
            return False
    
        reverseNum = 0
        while(x > reverseNum):
            # 拿出原数的前半部分反序，然后和剩余后半部分进行比较
            # 循环内，原数一直在/10变小，新数一直在变大
            # 当原数小于新数，那么原数的前半部分已经放到了新数里面
            reverseNum = int(reverseNum * 10 + x % 10)
            x = int(x / 10)

        return x == reverseNum or x == int(reverseNum/10)
        # 12 == 123 or 12 == int(12.3)
        # 12 == 12  or 12 == int(1.2)
        # 原数为偶数，直接判断相等
        # 原数为奇数，那么需要去掉中间的数在进行判断
        # 如何去除？新数大于原数剩余，所以中间部分肯定在新数里，那么直接去掉新数的最后一位，即是中间数

test = Solution()
print(test.isPalindrome(12321))