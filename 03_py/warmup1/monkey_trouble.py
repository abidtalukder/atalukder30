"""
Codingbat Warmup-1 monkey_trouble
"""
def monkey_trouble(a_smile, b_smile):
    """
    We have two monkeys, a and b, and the parameters a_smile and b_smile
    indicate if each is smiling. We are in trouble if they are both smiling
    or if neither of them is smiling. Return True if we are in trouble.
    """
    return a_smile == b_smile

def main():
    """
    Main function
    """
    print(monkey_trouble(True, True))
    print(monkey_trouble(False, False))
    print(monkey_trouble(True, False))

if __name__ == "__main__":
    main()
