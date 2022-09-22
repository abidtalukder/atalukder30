"""
Codingbat Warmup-1 not_string
"""
def not_string(str):
    if str[:3] == 'not':
        return str
    else:
        return 'not ' + str

if __name__ == '__main__':
    print(not_string('candy'))
    print(not_string('x'))
    print(not_string('not bad'))
