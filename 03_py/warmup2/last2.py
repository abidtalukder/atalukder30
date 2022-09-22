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

if __name__ == "__main__":
    print(last2('hixxhi'))
    print(last2('xaxxaxaxx'))
    print(last2('axxxaaxx'))
