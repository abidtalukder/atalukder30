"""
Codingbat List-1 common_end
"""
def common_end(a, b):
    """
    Given 2 arrays of ints, a and b, return True if they have the same first
    element or they have the same last element. Both arrays will be length 1 or
    more.
    """
    return a[0] == b[0] or a[-1] == b[-1]

"""
Codingbat List-2 centered_average
"""
def centered_average(nums):
    """
    Return the "centered" average of an array of ints, which we'll say is the
    mean average of the values, except ignoring the largest and smallest values
    in the array. If there are multiple copies of the smallest value, ignore just
    one copy, and likewise for the largest value. Use int division to produce the
    final average. You may assume that the array is length 3 or more.
    """
    return (sum(nums) - max(nums) - min(nums)) // (len(nums) - 2)

"""
Codingbat List-2 count_evens
"""
def count_evens(nums):
    """
    Return the number of even ints in the given array.
    """
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

"""
Codingbat List-2 has22
"""

def has22(nums):
    """
    Given an array of ints, return True if the array contains a 2 next to a 2
    somewhere.
    """
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False


"""
Codingbat List-2 sum13
"""
def sum13(nums):
    """
    Return the sum of the numbers in the array, returning 0 for an empty
    array. Except the number 13 is very unlucky, so it does not count and
    numbers that come immediately after a 13 also do not count.
    """
    sum = 0
    skip = False
    for i in nums:
        if i == 13:
            skip = True
        elif skip:
            skip = False
        else:
            sum += i
    return sum

"""
Codingbat List-2 sum67
"""
def sum67(nums):
    """
    Return the sum of the numbers in the array, except ignore sections of
    numbers starting with a 6 and extending to the next 7 (every 6 will be
    followed by at least one 7). Return 0 for no numbers.
    """
    sum = 0
    skip = False
    for i in nums:
        if i == 6:
            skip = True
        if not skip:
            sum += i
        if i == 7:
            skip = False
    return sum