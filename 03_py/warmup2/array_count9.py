"""
Codingbat Warmup-2 array_count9
"""
def array_count9(nums):
    """
    Given an array of ints, return the number of 9's in the array.
    """
    return nums.count(9)

if __name__ == "__main__":
    print(array_count9([1, 2, 9]))
    print(array_count9([1, 9, 9]))
    print(array_count9([1, 9, 9, 3, 9]))


