#_*_coding:utf-8_*_
'''
    剑指offer  11   旋转数组的最小数字

    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的
    一个旋转，输出旋转数组的最小元素。例如，数组[3, 4, 5, 1, 2] 为 [1, 2, 3, 4, 5] 的一个旋转，
    该数组的最小值为1。


示例 1：
    输入：[3,4,5,1,2]
    输出：1

示例 2：
    输入：[2,2,2,0,1]
    输出：0
'''
from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        '''
            复杂度分析：
                时间复杂度为O(n)
                空间复杂度为O(1)
        '''
        minNumber = 1e9
        for i in numbers:
            if i < minNumber:
                minNumber = i
        return minNumber


    def minArray1(self, numbers: List[int]) -> int:
        '''
            如下图所示，寻找旋转数组的最小元素即为寻找右
            排序数组的首个元素 nums[x] 称为 x的旋转点。

            排序数组的查找问题，首先考虑使用二分法解决
            其可将遍历法的线性级别时间复杂度降为对数级别

            算法流程：
                1，初始化：声明i, j 双指针分别指向 nums 数组左右两端
                2，循环二分：设 mid = (i+j)/2 为每次二分的中点，分为下面三种情况：
                    1，当 nums[mid] > nums[j] m 一定在左排序数组中，即旋转点 x一定
                        在 [m+1, j] 闭区间内，因此执行 i=m+1
                    2，当 nums[mid] < nums[j] m 一定在右排序数组中，即旋转点 x 一定
                        在 [i, m] 闭区间内，因此执行 j=m-1
                    3，当 nums[m] = nums[j] 无法判断 m 在那个排序数组中，即无法判断
                        旋转点 x 在[i, m] 还是 [m+1, j]区间
                        解决方案：执行 j=j-1 缩小判断范围
                3，返回值：当 i=j时跳出二分循环，并返回旋转点的值 nums[i]


            时间复杂度：O(logn)
            空间复杂度：O(1)
        '''
        i, j = 0, len(numbers)-1
        while i<j:
            m = (i+j)//2
            if numbers[m] > numbers[j]:
                i = m+1
            elif numbers[m] < numbers[j]:
                j = m
            else:
                j-=1
        return numbers[i]
























