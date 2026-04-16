class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        dup=x
        sum=0
        while dup:
            sum=sum+dup%10
            dup=dup//10
        return sum if x%sum==0 else -1