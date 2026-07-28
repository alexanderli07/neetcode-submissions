class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeroes = 0
        for i in nums:
            if i == 0:
                zeroes += 1
            else:
                total = total * i

        arr = []
        if zeroes >= 2:
            return [0] * len(nums)
        elif zeroes == 1:
            for j in nums:
                if j == 0:
                    arr.append(int(total))
                else:
                    arr.append(0)
        else:
            for j in nums:
                arr.append(int(total / j))

        return arr

        