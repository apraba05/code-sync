from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(list)
        another_one = defaultdict(int)
        arr = [0]*k

        for i in range (len(nums)):
            freq[nums[i]].append(i)
            
        for i in freq:
            another_one[i] = len(freq[i])
        
        sorted_another_one = sorted(another_one.items(), key=lambda x:x[1], reverse=True)
        new_sort = dict(sorted_another_one)

        values = tuple(new_sort.keys())
        while k != 0:
            for i in range (len(arr)):
                arr[i] = values[i]
            k -= 1
            continue
        
        return(arr)