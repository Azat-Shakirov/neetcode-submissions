class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        set1 = set([])
        nums.sort()
        for i in range(len(nums) - 1):
            l, r = i + 1, len(nums) - 1
            while l < r:
                t = tuple([nums[i], nums[l], nums[r]])
                if t in set1:
                    l += 1
                    r -= 1
                    continue
                if nums[l] + nums[r] < 0 - nums[i]:
                    l += 1
                elif nums[l] + nums[r] > 0 - nums[i]:
                    r -= 1
                else:
                    triplets.append(list(t))
                    set1.add(t)
                    l += 1
                    r -= 1
        return triplets