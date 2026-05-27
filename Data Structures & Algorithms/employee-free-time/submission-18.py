# Definition for an Interval.
# class Interval:
#     def __init__(self, start: int = None, end: int = None):
#         self.start = start
#         self.end = end
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []

        for employee in schedule:
            for interval in employee:
                intervals.append([interval.start, interval.end])
#[x,y]，[x,y]靠看前面x来排
        intervals.sort(key=lambda x: x[0])
#合并区间，用0组跟1...n一个一个比较
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]#第0个数组的后面数默认为last_end,[0,1]的1

            if start <= last_end:#[0,1],[3,4]->3<1,不是就插入[3,4]。（1],[3）,因为merged只有他一个
                merged[-1][1] = max(last_end, end)#换一个，如果成立1<4=4->变成[0,4]。如果上面一行还继续大，就叫第二个数的第二个来跟他比谁大。这个是last_end之前的值
            else:
                merged.append([start, end])#插入去并存
#找出了空隙区间
        free = []

        for i in range(1, len(merged)):#这里的merged默认是有0的，但是要从1开始
            prev_end = merged[i - 1][1]#[0,1][1,2]=1,跟前面函数的last_end定义一样,不过要前面i-1
            curr_start = merged[i][0]#[1,2]=1，又像上面一样拿,1][1,

            if prev_end < curr_start:#1<1,no
                free.append(Interval(prev_end, curr_start))

        return free