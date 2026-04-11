class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        freq_list = [(y,x) for x,y in freq.items()]
        freq_list.sort(reverse=True)
        return [x[1] for x in freq_list[0:k]]

        