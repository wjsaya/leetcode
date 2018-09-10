#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Author:	wjsaya(http://www.wjsaya.top) 
# @Date:	2018-09-10 08:14:28 
# @Last Modified by:	wjsaya(http://www.wjsaya.top) 
# @Last Modified time:	2018-09-10 08:47:37 
 

# https://leetcode-cn.com/problems/integer-to-roman/description/
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
class Solution:
    # 给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
    # 1 --> 3999，最高位最大为3000，去掉了最高位的判断
    # 然后从左到右扫描，排除特殊情况。
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        re = ''
        count_thousands = num // 1000
        if count_thousands > 0:
            re += 'M' * count_thousands
            num %= 1000
        
        count_hundreds = num // 100
        if count_hundreds > 0:
            if count_hundreds == 9:
                re += 'CM'
            elif count_hundreds >= 5:
                re += 'D' + 'C' * (count_hundreds - 5)
            elif count_hundreds == 4:
                re += 'CD'
            else:
                re += 'C' * count_hundreds
            num %= 100


        count_tens = num // 10
        if count_tens > 0:
            if count_tens == 9:
                re += 'XC'
            elif count_tens >= 5:
                re += 'L' + 'X' * (count_tens - 5)
            elif count_tens == 4:
                re += 'XL'
            else:
                re += 'X' * count_tens
            num %= 10

        
        count_digits = num
        if count_digits > 0:
            if count_digits == 9:
                re += 'IX'
            elif count_digits >= 5:
                re += 'V' + 'I' * (count_digits - 5)
            elif count_digits == 4:
                re += 'IV'
            else:
                re += 'I' * count_digits
            num %= 10

        return re

test = Solution()
print(test.intToRoman(60))
