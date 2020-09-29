def main():
    # Get a sentence from user
    sent = input('Enter  a sentence: ')
    # take the first char in this sentence
    new_sent = sent[0]

    # loop over elements of sentence
    for i in sent[1:]:
        # i in uppercase
        if i.isupper():
            new_sent += ' ' + i.lower()
        else:
            new_sent += i

    print(new_sent)


main()

