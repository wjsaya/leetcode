#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Author:	wjsaya(http://www.wjsaya.top) 
# @Date:	2018-08-19 17:11:47 
# @Last Modified by:	wjsaya(http://www.wjsaya.top) 
# @Last Modified time:	2018-08-19 22:29:08 
  

# 题目地址:https://leetcode-cn.com/problems/roman-to-integer/
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
# 罗马数字包含以下七种字符：I， V， X， L，C，D 和 M
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例
#   例如 4 不写做 IIII，而是 IV。
#   数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
#   数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况： 

#     I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
#     X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
#     C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        additDict = {
            # 加法值字典
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        subtractDict = {
            # 减法值字典
            'CM' : 100,
            'CD' : 100,
            'XC' : 10,
            'XL' : 10,
            'IX' : 1,
            'IV' : 1
        }

        for i in additDict:
            # 首先累加每个单独的字母对应的值，不管特殊规则
            total += additDict[i] * s.count(i)

        for j in subtractDict:
            # 累加时会出现多加的情况
            # 如果有多加的，减去 (多加的值 * 字母数 * 2) 即可
            # 如果没有出现subtractDict中的值，那么 *0次 不会更改原结果
            #       *2？假如出现了AB
                    # AB实际等于B-A
                    # 累加，AB变成了A+B，因此少了一个-A，目前，结果暂时为A+B-A
                    # 其次，累加A+B还多加了一次A，需要减去，最终结果为(A+B)-A-A
                    # 所以累加之后需要减去两次A
        #    数学方法证明:
        #         实际：AB = B - A
        #         本段实例：
        #             AB  = A + B - A * 2
        #                 = A + B - A - A
        #                 = B - A
        #                 = 实际结果
            total -= subtractDict[j] * 2 * s.count(j)
        return total

test = Solution()
print(test.romanToInt("MCMXCIV"))