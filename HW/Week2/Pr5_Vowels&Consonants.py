def main():
    # ask user to input a string
    string = input('Enter your string: ').lower()
    # initialise vowel variable
    vowels = 0
    # initialise consonant variable
    consonants = 0
    # loop over char in string
    for i in string:
        # count vowel
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
             vowels += 1
        # count consonant
        else:
             consonants += 1
    print('Total number of Vowels in this string is: ', vowels)
    print('Total number of  Consonant in this string is: ',  consonants)


main()

