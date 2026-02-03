from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        minHeap = []
        freq = Counter(words)

        for word, count in freq.items():
            minHeap.append([-count,word])

        heapq.heapify(minHeap)

        print(minHeap)

        result = []

        while k > 0:
            result.append(heapq.heappop(minHeap)[1])
            k -= 1
        
        return result