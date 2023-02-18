def fibonacci_sequence(num):
    """Simple recursive function that finds Fibonacci numbers based on user input"""
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return (fibonacci_sequence(num - 2) +fibonacci_sequence(num - 1))

def main ():
    """Main function for testing purposes"""
    num = int(input("\nPlease enter how many instances of a Fibonacci sequence you'd like to see: "))
    for num in range(0, num):
        print(fibonacci_sequence(num))

if __name__ == '__main__':
    main()