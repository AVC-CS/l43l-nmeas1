def main():
    total = 0
    numbers = [0]*5

    for i in range(len(numbers)):
        numbers[i] = int(input('Enter a number: '))
        total += numbers[i]
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
