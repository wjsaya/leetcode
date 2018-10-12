#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Author:	wjsaya(http://www.wjsaya.top) 
# @Date:	2018-08-21 21:06:40 
# @Last Modified by:	wjsaya(http://www.wjsaya.top) 
# @Last Modified time:	2018-08-21 23:15:03 

 
# 题目地址:https://leetcode-cn.com/problems/valid-parentheses/
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：

#     左括号必须用相同类型的右括号闭合。
#     左括号必须以正确的顺序闭合。

# 注意空字符串可被认为是有效字符串。
# 输入: "()"
# 输出: true

# 输入: "()[]{}"
# 输出: true

# 输入: "(]"
# 输出: false

# 输入: "([)]"
# 输出: false

# 输入: "{[]}"
# 输出: true

class Solution:
    def isValid(self, s):
        dict = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        left = []

        for i in str(s):
            if i in ['(', '[', '{']:
                # 遇到左半边，追加到left列表
                left.append(i)

            if i in [')', ']', '}']:
                # 遇到右半边，和左半边第一个进行比对
                # 能配对，继续
                # 配对失败，返回False
                if len(left) == 0 or left.pop(-1) != dict[i]:
                    return False

        if len(left) != 0:
            # 到了这里，left列表应该全部pop完毕才对
            # 有剩余？那就是有某些左半边符号未被匹配上，返回False
            return False

        return True

instr = "(("
test = Solution()
print(test.isValid(instr))  