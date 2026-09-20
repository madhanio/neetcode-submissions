class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in nums: 
            if i in hashset:
                return True
            hashset.add(i)
        return False