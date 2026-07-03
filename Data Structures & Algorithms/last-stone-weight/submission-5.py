class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            first = stones.pop()
            second = stones.pop()
            if first == second:
                pass
            if first < second:
                second = second - first
                stones.append(second)
            if first > second:
                first = first - second
                stones.append(first)
            self.lastStoneWeight(stones)
        if stones:
            return stones[0]
        else:
            return 0