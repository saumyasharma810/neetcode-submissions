class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        freq_bucket = [[] for _ in range(n+1)]
        for i,j in freq.items():
            freq_bucket[j].append(i)
        print(freq_bucket)
        topKFreq = []
        # k, bucket, topKFreq
        for i in reversed(range(n+1)):
            for j in freq_bucket[i]:
                topKFreq.append(j)
                if len(topKFreq) == k:
                    return topKFreq
                




        # // O(nlogn) -> klogn heap -> o(n) bucket
        # // o(n)

        