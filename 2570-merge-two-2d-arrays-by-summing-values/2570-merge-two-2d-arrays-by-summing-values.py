class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # answer = []
        # total = nums1+nums2
        # for i in range(len(total)):
        #     for j in range(i+1,len(total)):
        #         if total[i][0] == total[j][0]:
        #             answer.append([total[i][0],total[i][1]+total[j][1]])
        #             nums1.remove(total[i])
        #             nums2.remove(total[j])
        # return sorted(answer+nums1+nums2)
        dict = defaultdict(int)
        for id,val in nums1 + nums2:
            if id in dict:
                dict[id] += val
            else:
                dict[id] = val
        return sorted(list(dict.items()))