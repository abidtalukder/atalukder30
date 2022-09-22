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


"""
Codingbat Warmup-2 array_count9
"""
def array_count9(nums):
    """
    Given an array of ints, return the number of 9's in the array.
    """
    return nums.count(9)


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

"""
Codingbat Warmup-2 front_times
"""
def front_times(str, n):
    """
    Given a string and a non-negative int n, we'll say that the front of the
    string is the first 3 chars, or whatever is there if the string is less
    than length 3. Return n copies of the front;
    """
    if len(str) < 3:
        return str * n
    else:
        return str[:3] * n

"""
Codingbat Warmup-2 last2
"""
def last2(str):
    """
    Given a string, return the count of the number of times that a substring
    length 2 appears in the string and also as the last 2 chars of the string,
    so "hixxxhi" yields 1 (we won't count the end substring).
    """
    if len(str) < 2:
        return 0
    count = 0
    last2 = str[-2:]
    for i in range(len(str)-2):
        if str[i:i+2] == last2:
            count += 1
    return count


"""
Codingbat Warmup-2 string_bits
"""
def string_bits(str):
    return str[::2]

"""
Codingbat Warmup-2 string_match
"""
def string_match(a, b):
    """
    Given 2 strings, a and b, return the number of the positions where they
    contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3,
    since the "xx", "aa", and "az" substrings appear in the same place in both
    strings.
    """
    count = 0
    for i in range(len(a)):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count


"""
Codingbat Warmup-2 string_splosion
"""
def string_splosion(str):
    """
    Given a non-empty string like "Code" return a string like "CCoCodCode".
    """
    return ''.join([str[:i] for i in range(len(str)+1)])

    """
Codingbat Warmup-2 string_times
"""
def string_times(str, n):
    return str * n