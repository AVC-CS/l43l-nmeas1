def main():
    total = 0
    count = 0
    mylist = [0] *5
    while count < 5:
        numbers = int(input('Enter a number: '))
        mylist.append(numbers)
        total += numbers
        count += 1

    #numbers = [0] * 5
    #for i in range(len(numbers)):
    #    numbers[i] = int(input('Enter a value: '))

    """
    ########################################
    Code Your Program here
    ########################################
    """

    #total = sum(numbers)
    print(total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total, numbers


if __name__ == '__main__':
    main()
