class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = []

        for i in arr:
            closestElement = i - x
            minHeap.append([closestElement,i])
            
        
        heapq.heapify(minHeap)

        result = []

        while k > 0:
            closest, element = heapq.heappop(minHeap)
            result.append(element)
            k -= 1
        
        return result