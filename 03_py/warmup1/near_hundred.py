"""
Codingbat Warmup-1 near_hundred
"""
def near_hundred(n):
    if n >= 90 and n <= 110:
        return True
    elif n >= 190 and n <= 210:
        return True
    else:
        return False

if __name__ == "__main__":
    print(near_hundred(93))
    print(near_hundred(90))
    print(near_hundred(89))

