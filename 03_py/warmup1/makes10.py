"""
Codingbat Warmup-1 makes10
"""
def makes10(a, b):
    return (a == 10 or b == 10 or a + b == 10)

if __name__ == "__main__":
    print(makes10(9, 10))
    print(makes10(9, 9))
    print(makes10(1, 9))
