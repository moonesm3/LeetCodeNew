class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        values = set(nums)
        pair_xors = set()
        for first in values:
            for second in values:
                pair_xors.add(first ^ second)
        triplet_xors = set()
        for pair_xor in pair_xors:
            for third in values:
                triplet_xors.add(pair_xor ^ third)
        return len(triplet_xors)