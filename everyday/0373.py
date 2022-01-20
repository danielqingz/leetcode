# 给定两个以 升序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。

# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。

# 请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq, ans = [(num + nums2[0], i, 0) for i, num in enumerate(nums1[:k])], []
        heapq.heapify(pq)
        while pq and k:
            _, i, j = heapq.heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j < len(nums2) - 1:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1
        return ans
        
