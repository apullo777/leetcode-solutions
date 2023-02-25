# https://leetcode.com/problems/top-k-frequent-elements/

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Input: nums = [1], k = 1
# Output: [1]

# Solution 1: collections.Counter.most_common()
# most_common() takes O(n log n)
# Counter() taks O(n)

# Time: O(n log n)
# Space: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_common = Counter(nums).most_common()
        ans = []
        
        for i in range(k):
            ans.append(most_common[i][0])
        
        return ans

# Solution 2: Heap sort
# Time: O(N + KlogN), where N <= 10^5 is length of nums array, K <= N.
# heapify(maxHeap) costs O(N)
# heappop(maxHeap) k times costs O(KlogN)
# Space: O(N)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        maxHeap = [[-freq, num] for num, freq in cnt.items()]
        heapify(maxHeap)
        
        ans = []
        for i in range(k):
            _, num = heappop(maxHeap) # Pop and return the smallest item from the heap
            ans.append(num)
        return ans

# Solution 3: Bucket sort

# Since the array nums has size of n, the frequency can be up to n.
# We can create bucket to store numbers by frequency.
# Then start bucketIdx = n, we can get the k numbers which have largest frequency.

# Time: O(N), where N <= 10^5 is length of nums array.
# Space: O(N)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        for num, freq in cnt.items():
            bucket[freq].append(num)
            
        bucketIdx = n
        ans = []
        while k > 0:
            while not bucket[bucketIdx]:  # Skip empty bucket
                bucketIdx -= 1
                
            for num in bucket[bucketIdx]:
                if k == 0: break
                ans.append(num)
                k -= 1
            bucketIdx -= 1
        return ans