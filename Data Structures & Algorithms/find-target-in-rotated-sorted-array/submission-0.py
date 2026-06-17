class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            while l <= r:
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid

            return -1

        else:
            part = ''
            if target < nums[0]:
                part = 'sec'
            else:
                part = 'first'

            while l <= r:
                mid = (l+r)//2
                if nums[mid] >= nums[0]:
                    if part == 'first':
                        if nums[mid] < target:
                            l = mid + 1
                        elif nums[mid] > target:
                            r = mid - 1
                        else:
                            return mid
                    else:
                        l = mid + 1

                else:
                    if part == 'sec':
                        if nums[mid] < target:
                            l = mid + 1
                        elif nums[mid] > target:
                            r = mid - 1
                        else:
                            return mid
                    else:
                        r = mid - 1

            return -1