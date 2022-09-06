# https://leetcode.com/problems/minimum-number-of-refueling-stops/

# Input: target = 1, startFuel = 1, stations = []
# Output: 0
# Explanation: We can reach the target without refueling.

# Input: target = 100, startFuel = 1, stations = [[10,100]]
# Output: -1
# Explanation: We can not reach the target (or even the first gas station).

# Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
# Output: 2
# Explanation: We start with 10 liters of fuel.
# We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
# Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
# and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
# We made 2 refueling stops along the way, so we return 2.

# Priority queue 
# Time: O(NlogN)

# We add all reachable stop to priority queue.
# We pop out the largest gas from pq and refeul once.
# If we can't refuel, means that we can not go forward and return -1

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        res = i = 0
        while startFuel < target:
            while i < len(stations) and stations[i][0] <= startFuel:
                heapq.heappush(pq, -stations[i][1])
                i += 1
            if not pq: return -1
            startFuel += -heapq.heappop(pq)
            res += 1
        return res