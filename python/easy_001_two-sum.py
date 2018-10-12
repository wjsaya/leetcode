#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Author:	wjsaya(http://www.wjsaya.top) 
# @Date:	2018-08-18 22:18:33 
# @Last Modified by:	wjsaya(http://www.wjsaya.top) 
# @Last Modified time:	2018-08-19 12:18:47 

# 题目地址:https://leetcode-cn.com/problems/two-sum/
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# 。。。只想到穷举法

class Solution:
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        穷举，太耗时间。O(n) * O(n-1)
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums, target):   
        '''
        遍历传入所有值 \n
        存入字典，字典中关系如下： \n
        tempDict[ target - valueNow ] = i \n
        '''
        # list，TOfind
        # 根据数组下标i(0-->n)遍历原数组，值放入valueNow
        # 找dict[valueNow]
        #   如果找到了
        #       说明valueNow是另一个数的互补数
        #       因此待返回的下标是 TOfind-valueNow 的下标与 valueNow 的下标
        #       即  dict[valueNow] 和 i ，构建一个字典直接返回即可。
        #       return [dict[valueNow], i]
        # 	如果没找到
        #       那么valueNow暂时没有互补数，将其存入字典dict[TOfind-valueNow] , 值为 当前下标。

        tempDict = {}
        for i in range(len(nums)):
            valueNow = nums[i]
            
            if valueNow in tempDict:
                return [tempDict[valueNow], i]
            else:
                tempDict[target - valueNow] = i



numlist = [3, 2, 4]
test = Solution()
print(test.twoSum(numlist, 6))
