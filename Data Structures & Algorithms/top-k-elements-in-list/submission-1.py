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
            print(i)
            if freq_bucket[i]:
                print(freq_bucket[i])
                j = 0
                while len(topKFreq) < k and j < len(freq_bucket[i]):
                    topKFreq.append(freq_bucket[i][j])
                    j+=1
                if len(topKFreq) == k:
                    return topKFreq
                




        # // O(nlogn) -> klogn heap -> o(n) bucket
        # // o(n)

        