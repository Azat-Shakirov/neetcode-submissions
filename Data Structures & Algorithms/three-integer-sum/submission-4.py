class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        set1 = set([])
        nums1 = sorted(nums)
        for i in range(len(nums1) - 1):
            l, r = i + 1, len(nums1) - 1
            while l < r:
                t = tuple([nums1[i], nums1[l], nums1[r]])
                if t in set1:
                    l += 1
                    r -= 1
                    continue
                if nums1[l] + nums1[r] < 0 - nums1[i]:
                    l += 1
                elif nums1[l] + nums1[r] > 0 - nums1[i]:
                    r -= 1
                else:
                    triplets.append(t)
                    set1.add(t)
                    l += 1
                    r -= 1
        return triplets