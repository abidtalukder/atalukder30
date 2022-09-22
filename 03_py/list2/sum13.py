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

def main():
    """
    Main function
    """
    print(sum13([1, 2, 2, 1]))
    print(sum13([1, 1]))
    print(sum13([1, 2, 2, 1, 13]))
    
if __name__ == "__main__":
    main()

