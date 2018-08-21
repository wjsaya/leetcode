#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Author:	wjsaya(http://www.wjsaya.top) 
# @Date:	2018-08-19 22:29:22 
# @Last Modified by:	wjsaya(http://www.wjsaya.top) 
# @Last Modified time:	2018-08-21 15:45:37 
 
 
# 题目地址:https://leetcode-cn.com/problems/longest-common-prefix/
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 示例 1:

# 输入: ["flower","flow","flight"]
# 输出: "fl"

# 示例 2:

# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。

# 说明:

# 所有输入只包含小写字母 a-z 。


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        # 空列表，直接返回""
        if len(strs) == 1:
            return strs[0]
        # 列表只有一个字符串，直接返回

        longIndex = 0
        min_len = len(min(strs))
        for num in range(min_len):
            # 遍历传入字符串组中最短的那个
            for each in range(1, len(strs)):
                if strs[each][num] == strs[each-1][num]:
                    longIndex = num
        
        print(strs[0][0:longIndex])

li = ["acb", "acd", "ac"]
test = Solution()
print("|", test.longestCommonPrefix(li), "|")