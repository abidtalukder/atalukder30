"""
Codingbat Warmup-1 diff21
"""
def diff21(n):
    """
    Given an int n, return the absolute difference between n and 21,
    except return double the absolute difference if n is over 21.
    """
    if n > 21:
        return (n - 21) * 2
    return 21 - n

if __name__ == "__main__":
    print(diff21(19))
    print(diff21(10))
    print(diff21(21))
