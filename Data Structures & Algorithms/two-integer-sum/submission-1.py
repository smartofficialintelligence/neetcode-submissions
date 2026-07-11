class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate array
        # store idx, val in hash
        # compute complement, check if in hash
        # check if the complement is in the hash map.
        # if found, return both indices.
        # otherwise, store values
        seen = {}
        for i, v in enumerate(nums):
            compliment = target - v
            if compliment in seen:
                return [seen[compliment],i]
            seen[v] = i