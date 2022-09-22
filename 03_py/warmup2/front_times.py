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

if __name__ == "__main__":
    print(front_times('Chocolate', 2))
    print(front_times('Chocolate', 3))
    print(front_times('Abc', 3))

