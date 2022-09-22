"""
Codingbat Warmup-2 array123
"""
def array123(nums):
    """
    Given an array of ints, return True if the sequence of numbers 1, 2, 3
    appears in the array somewhere.
    """
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

def main():
    """
    Test function
    """
    array = [1, 1, 2, 3, 1]
    print(array123(array))

if __name__ == "__main__":
    main()
