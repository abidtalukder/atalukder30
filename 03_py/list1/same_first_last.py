"""
Codingbat List-1 same_first_last
"""
def same_first_last(nums):
    """
    Given an array of ints, return True if the array is length 1 or more,
    and the first element and the last element are equal.
    """
    return len(nums) >= 1 and nums[0] == nums[-1]

def main():
    print(same_first_last([1, 2, 3]))
    print(same_first_last([1, 2, 3, 1]))
    print(same_first_last([1, 2, 1]))

if __name__ == "__main__":
    main()
