def main():
    # Enter the user's name
    full_name = input('Enter your full name: ')
    # Split name by a space delimiter
    name = full_name.split(' ')
    for i in range(len(name)):
        # take the first char in ech element
        name[i] = name[i][0:1]
    # using '.' to separate char
    name = '.' .join(name)
    print(name.upper())


main()
