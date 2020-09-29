def main():
    # Get a string, split element by space
    sent = input('Enter sentence: ').split()

    for i in sent:
        # i in lowercase
        if (i[1:].islower()):
             print(i[1:] + i[0] + 'ay', end=" ")
        #i in uppercase
        else:
             print(i[1:] + i[0] + 'AY', end=" ")
    # print the result on screen
    print()


main()


