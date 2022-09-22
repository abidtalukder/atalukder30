"""
Codingbat Warmup-1 missing_char
"""
def missing_char(str, n):
    return str[:n] + str[n+1:]

if __name__ == "__main__":
    print(missing_char('kitten', 1))
    print(missing_char('kitten', 0))
    print(missing_char('kitten', 4))
