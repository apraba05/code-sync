from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        freq = Counter(words)

        for word, counter in freq.items():
            heap.append([-counter,word])
        

        heapq.heapify(heap)
        result = []

        while k > 0:
            value, word = heapq.heappop(heap)
            result.append(word)
            k -= 1
        
        return result