def main():
    total = 0
    numbers = []

    for x in range(5):
        numlist = int(input('Enter a number: '))
        numbers.append(numlist)
        total += numlist
    print(total)

    """
    ########################################
    Code Your Program here
    ########################################
    """

    #total = sum(numbers)
    #print(total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total, numbers


if __name__ == '__main__':
    main()
