# this is leet code problem solution (198. House Robber)

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    # Initialize two variables to keep track of the maximum amount robbed at each house
    max_money_at_house = [0] * len(nums)

    # The maximum money at the first house is the money at the first house itself
    max_money_at_house[0] = nums[0]

    # The maximum money at the second house is the maximum of the money at the first and second houses
    max_money_at_house[1] = max(nums[0], nums[1])

    # Iterate through the remaining houses, calculating the maximum money at each house
    for i in range(2, len(nums)):
        max_money_at_house[i] = max(max_money_at_house[i - 1], max_money_at_house[i - 2] + nums[i])

    # The maximum money that can be robbed is the last element of the max_money_at_house array
    return max_money_at_house[-1]

# Example usage:
nums = [2, 7, 9, 3, 1]
result = rob(nums)
print(result)  # This should print 12

