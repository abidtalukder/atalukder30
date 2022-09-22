"""
Codingbat List-1 first_last6
"""
def first_last6(nums):
    """
    Given an array of ints, return True if 6 appears as either the first or last
    element in the array. The array will be length 1 or more.
    """
    return nums[0] == 6 or nums[-1] == 6

def main():
    """
    Main function
    """
    print(first_last6([1, 2, 6]))
    print(first_last6([6, 1, 2, 3]))
    print(first_last6([13, 6, 1, 2, 3]))

if __name__ == "__main__":
    main()
