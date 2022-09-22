"""
Codingbat Warmup-2 array_front9
"""
def array_front9(nums):
    """
    Given an array of ints, return True if one of the first 4 elements in the
    array is a 9. The array length may be less than 4.
    """
    if len(nums) > 4:
        nums = nums[:4]
    return 9 in nums

if __name__ == "__main__":
    print(array_front9([1, 2, 9, 3, 4]))
    print(array_front9([1, 2, 3, 4, 9]))
    print(array_front9([1, 2, 3, 4, 5]))
