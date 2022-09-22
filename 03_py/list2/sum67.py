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

def main():
    """
    main function
    """
    print(sum67([1, 2, 2]))
    print(sum67([1, 2, 2, 6, 99, 99, 7]))
    print(sum67([1, 1, 6, 7, 2]))

if __name__ == "__main__":
    main()
