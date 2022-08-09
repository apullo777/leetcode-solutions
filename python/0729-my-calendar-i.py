# https://leetcode.com/problems/my-calendar-i/

# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]

# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

class MyCalendar:

    def __init__(self):
        self.intervals = []
        
    def book(self, start: int, end: int) -> bool:
        if end <= start:
            return False
        
        i = bisect.bisect_right(self.intervals, start)
        if i % 2:   # start is in some stored interval
            return False
        
        j = bisect.bisect_left(self.intervals, end)
        if i != j:
            return False
        
        self.intervals[i:i] = [start, end]
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)