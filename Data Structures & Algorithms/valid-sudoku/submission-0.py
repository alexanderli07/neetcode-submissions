class Solution:
    def hasDupe(self, nums):
        nums = [item for item in nums if item != "."]
        nums.sort()
        for n in range(len(nums) - 1):
            if nums[n] == nums[n+1]:
                return True

        return False


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for a in board:
            if self.hasDupe(a):
                return False
        
        for c in range(9):
            arr = []
            for r in board:
                arr.append(r[c])
            
            if self.hasDupe(arr):
                return False

        start = 0
        stop = 3
        arr = []
        for _ in range(3):
            for c in range(9):
                for r in range(start, stop):
                    arr.append(board[c][r])

                # print(arr, c)
                if c == 2 or c == 5 or c == 8:
                    if self.hasDupe(arr):
                        return False
                    arr = []
                    if c == 8:
                        start += 3
                        stop += 3

        return True

        