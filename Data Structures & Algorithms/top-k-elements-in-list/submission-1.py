class Solution:
    def count(self, nums: List[int]):
        nums.sort()
        count = 1
        before = nums[0]
        arr = []
        for n in range(1, len(nums)):
            if nums[n] == before:
                count += 1
                before = nums[n]
            else:
                arr.append([before, count])
                count = 1
                before = nums[n]
        arr.append([before, count])
        arr.sort(key=lambda x: x[1], reverse=True)
        return arr




    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = self.count(nums)
        print(count)
        arr = []
        for i in range(k):
            arr.append(count[i][0])
        return arr

        