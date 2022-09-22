"""
Codingbat List-1 reverse3
"""
def reverse3(nums):
    """
    Given an array of ints length 3, return a new array with the elements in
    reverse order, so {1, 2, 3} becomes {3, 2, 1}.
    """
    return nums[::-1]

def main():
    """
    Main function
    """
    print(reverse3([1, 2, 3]))
    print(reverse3([5, 11, 9]))
    print(reverse3([7, 0, 0]))

if __name__ == "__main__":
    main()
