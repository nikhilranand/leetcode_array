class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        n=len(nums)
        element_sum=sum(nums)
        separated_digits = []   
        for num in nums:
            while num > 0:
                digit = num % 10  # Extract the last digit
                separated_digits.append(digit)
                num //= 10  # Remove the last digit from the number
        digit_sum=sum(separated_digits)
        return abs(element_sum - digit_sum)        
        #for num in nums:
        #    if num >= 10:  # Check if the number is two-digit
        #        digit1 = num // 10  # Extract the tens digit
        #        digit2 = num % 10  # Extract the ones digit
        #        separated_digits.append(digit1)
        #        separated_digits.append(digit2)
        #    else:
        #        separated_digits.append(num)  # Append single-digit numbers directly
        #digit_sum=sum(separated_digits)
        #return abs(element_sum - digit_sum)
        
        