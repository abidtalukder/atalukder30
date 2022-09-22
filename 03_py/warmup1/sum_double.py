"""
Codingbat Warmup-1 sum_double
"""
def sum_double(a, b):
    """
    Given two int values, return their sum. Unless the two values are the same,
    then return double their sum.
    """
    if a == b:
        return (a + b) * 2
    return a + b

if __name__ == "__main__":
    print(sum_double(1, 2))
    print(sum_double(3, 2))
    print(sum_double(2, 2))
