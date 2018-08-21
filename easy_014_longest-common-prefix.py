#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Author:	wjsaya(http://www.wjsaya.top) 
# @Date:	2018-08-19 22:29:22 
# @Last Modified by:	wjsaya(http://www.wjsaya.top) 
# @Last Modified time:	2018-08-21 21:00:33 
  
 
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
        if len(strs) == 0:
            return ""
        # 空列表，直接返回""
        if len(strs) == 1:
            return strs[0]
        # 列表只有一个字符串，直接返回

        # 从左向右取出列表中字符串的每一位字符进行比较
        #     相同，追加当前位的字符到返回字符串rsp，继续比较下一位
        #     不同，返回返回字符串rsp，结束运行
        min_len = self.get_minlen(strs)
        rsp = ''    # 初始化返回字符串
        for j in range(min_len):    # 指定字符串的遍历长度
            for i in range(len(strs)-1):    # 遍历字符串
                if strs[i][j] != strs[i+1][j]:  #发现不同，直接返回
                    return rsp

            rsp += strs[0][j]   # 当前位比较完毕，追加字符
        return rsp

    def get_minlen(self, strs):
        '''输入一个字符串数组
        返回数组中最短的字符串长度
        '''
        min_len = len(strs[0])
        for str in strs:
            if len(str) < min_len:
                min_len = len(str)
        return min_len
        

li = ["aca","acba"]
test = Solution()
print("|", test.longestCommonPrefix(li), "|")  