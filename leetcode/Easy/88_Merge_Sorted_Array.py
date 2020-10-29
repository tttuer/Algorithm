'''
nums1에 nums2 값을 넣는데 순서대로 정렬하는 방법
넣고 나서 정렬을 하는 방법과 투포인터를 이용해서 하는 방법이 있다.
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = 0
        for i in range(len(nums1)):
            if i1 >= len(nums2): break
            if nums1[i] == 0:
                nums1[i] = nums2[i1]
                i1 += 1
        nums1.sort()

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = len(nums1)-1
        i = m-1
        j = n-1
        
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[l] = nums1[i]
                l -= 1
                i -= 1
            else:
                nums1[l] = nums2[j]
                j -= 1
                l -= 1
        
        while i >= 0:
            nums1[l] = nums1[i]
            l -= 1
            i -= 1
        while j >= 0:
            nums1[l] = nums2[j]
            j -= 1
            l -= 1
            