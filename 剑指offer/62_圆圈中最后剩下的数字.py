#_*_coding:utf-8_*_
'''
题目：
    剑指offer 62  圆圈中最后剩下的数字

    0,1，....n-1这 n 个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字
    （删除后从下一个数字开始计数），求出这个圆圈里剩下的最后一个数字。

    例如0,1,2,3,4 这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个
    数字依次是2， 0， 4， 1，因此最后剩下的数字是3。

示例 1：
    输入: n = 5, m = 3
    输出: 3

示例 2：
    输入: n = 10, m = 17
    输出: 2
 
限制：
    1 <= n <= 10^5
    1 <= m <= 10^6

'''

# Python默认的递归深度不够，需要手动设置
sys.setrecursionlimit(1000000)

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        '''
            题目可以描述为：给定一个长度为 n 的序列，每次向后数 m 个元素并删除，
            那么最终留下的是第几个元素？

            如果我们知道对于一个长度 n-1的序列，留下的是第几个元素，那么我们就
            可以由此计算出长度为 n 的序列的答案。

            算法：
            首先，长度为 n 的序列会先删除第 m%n 个元素，然后剩下一个长度为 n-1
            的序列。那么我们可以递归的求解 f(n-1, m),就可以知道对于剩下的 n-1 个
            元素，最终会留下第几个元素，我们设答案为 x = f(n-1, m)

            由于我们删除了第 m%n 个元素，将序列的长度变为 n-1，当我们知道了 
            f(n-1, m) 对应的答案 x 之后，我们也就可以知道，长度为 n 的序列
            最后一个删除的元素，应当是从 m%n 开始数的第 x 个元素，因此也就有
            f(n, m) = (m %n + x)%n = (m+x)%n

            我们递归计算 f(n, m)， f(n-1, m) f(n-2, m).... 直到递归的终点
            f(1, m)，当序列长度为1 的时候，一定会留下唯一的那个元素，它的编号
            为0

            复杂度分析：
                时间复杂度：O(n)  需要求解的函数值有 n 个
                空间复杂度：O(n)  函数递归深度为n，需要使用O(n)的栈空间
        '''
        def f(n, m):
            if n==0:
                return 0
            x = f(n-1, m)
            return (m+x)%n

        return f(n, m)

    def lastRemaining1(self, n: int, m: int) -> int:
        '''
            上面递归可以改写为迭代，避免递归使用栈空间

            复杂度分析：
                时间复杂度：O(n)
                空间复杂度：O(1)  只使用常数个变量
        '''
        f = 0
        for i in range(2, n+1):
            f = (m+f)%i
        return f
