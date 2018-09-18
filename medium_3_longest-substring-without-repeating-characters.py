#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Author:	wjsaya(http://www.wjsaya.top) 
# @Date:	2018-09-10 08:54:53 
# @Last Modified by:	wjsaya(http://www.wjsaya.top) 
# @Last Modified time:	2018-09-10 08:54:53 
 
 
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/

# 给定一个字符串，找出不含有重复字符的最长子串的长度。

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        re_max = 0
        re = ''
        for i in s:
            print('\t\t', i)
            # 左向右扫描
            # 没有重复，计数器+1
            # 有重复，计数器清空，清空之前和max比较，取出大数
            if re.find(i) >= 0:
                re = ''
                re += i
                rec = len(re)
                if rec >= re_max:
                    re_max = rec
                print(re, re_max)

            else:
                re += i
                rec = len(re)
                if rec >= re_max:
                    re_max = rec
                print(re, re_max)
                
        return s, re, rec, re_max

test = Solution()
print(test.lengthOfLongestSubstring("dvdf"))
