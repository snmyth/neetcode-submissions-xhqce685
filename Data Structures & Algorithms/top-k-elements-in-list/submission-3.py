class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1

        a=  sorted(freq, key=lambda x: freq[x], reverse=True)
        print(a)


        b = []

        for i in range(k):
            b.append(a[i])

        return b