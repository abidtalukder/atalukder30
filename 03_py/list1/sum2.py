"""
Codingbat List-1 sum2
"""
def sum2(nums):
    """Return sum of first 2 elements of list"""
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + nums[1]

def main():
    """Main function"""
    print(sum2([1, 2, 3]))
    print(sum2([1, 1]))
    print(sum2([1, 1, 1, 1]))

if __name__ == "__main__":
    main()
