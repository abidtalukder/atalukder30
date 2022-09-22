"""
Codingbat Warmup-2 string_splosion
"""
def string_splosion(str):
    """
    Given a non-empty string like "Code" return a string like "CCoCodCode".
    """
    return ''.join([str[:i] for i in range(len(str)+1)])

if __name__ == '__main__':
    print(string_splosion('Code'))
    print(string_splosion('abc'))
    print(string_splosion('ab'))
