def main():
    from collections import Counter

    # Ask user input a string
    str = input("Enter a string: ")

    # count char appearing most in that string
    count = Counter(str).most_common(1)

    print("Character that appears most frequently in the string: ")
    print(count)


main()