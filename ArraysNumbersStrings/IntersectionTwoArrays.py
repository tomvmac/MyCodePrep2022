# Intersection Two Arrays

# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you
# may return the result in any order.

# General strategy
# 1. Iterate through nums1 and store count of each number in a hash table
# 2. Iterate through the nums2 and if the item value is found in the hash table, append to return array and decrement count from hash table

# Time: O(n)
# Space: O(n)

class Solution:
    def intersect(self, nums1, nums2):
        intersectArray = []
        numsCount = {}

        for i in range(len(nums1)):
            if nums1[i] not in  numsCount:
                numsCount[nums1[i]] = 1
            else:
                numsCount[nums1[i]] += 1

        for j in range(len(nums2)):
            if nums2[j] in numsCount:
                if numsCount[nums2[j]] > 0:
                    intersectArray.append(nums2[j])
                    numsCount[nums2[j]] -= 1


        return intersectArray

# Driver Code
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
# expected = [4, 9]

# nums1 = [1,2,2,1]
# nums2 = [2]
# expected = [2]

solution = Solution()

print(solution.intersect(nums1, nums2))



