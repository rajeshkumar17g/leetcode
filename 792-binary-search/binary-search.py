class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
                mid=(low+high)//2
                print("low:",low,"High:",high,"mid:",mid)
                if target==nums[mid]:
                    return mid
                elif target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
        return -1 # element not found
        