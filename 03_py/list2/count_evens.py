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

def main():
    """
    Test function
    """
    print(count_evens([2, 1, 2, 3, 4]))
    print(count_evens([2, 2, 0]))
    print(count_evens([1, 3, 5]))

if __name__ == "__main__":
    main()
