

def main():
    f = open('training.txt')
    data = f.read('training.txt')  # let's read the training dataset
    data.head()


    while True:
      i =str(input("Learning data file name?\n "
      "What would you like to do?\n"
      "1: Get the score of a word\n"
      "2: Get the average score of words in a file\n"
      "3; Find the hightest/ lowest scoring words in a file\n"
      "4: Sort the words in a file into positive.text and negative.txt\n"
      "5: Exit the program\n"
      "Enter a number 1-5:\t"))
      if i == "1":
          score_word()
      elif i == "2":
         avarage_score()
      elif i == "3":
         count_score()
      elif i == "4":
         sort_file()
      elif i == "5":
          break

main()

def sensitive(data):
    # set sentiment
    if data['Sentiment'] == 0:
        return 'negative'
    elif data['Sentiment'] == 1:
        return 'somewhat negative'
    elif data['Sentiment'] == 2:
        return 'neuteral'
    elif data['Sentiment'] == 3:
        return 'somewhat positive'
    else:
        return 'positive'
    data['index'] = data.apply(sensitive)

def getData(training):
    file = open(training)
    dictData = {}
    dataCount ={}
    lines = file.readlines()
    words = []
    for l in lines:
        w = l.strip().split(' ')
        words.append(w)
    for w in words:
        for index, w in enumerate(w):
            charList = [i for i in w]
            newWord = ''
            for input_char in w:
                if(charCheck(input_char) == 0):
                    charList.remove(input_char)
            for i in charList:
                newWord += i
            w[index] = newWord
    for word in words:
        word.remove(word[0])
    allword = []
    for index in range(len(words)):
        allword += words[index]
    setWord = set(allword)
    print(setWord)
    index = 0
    while index < len(allword):
         if dataCount[allword[index].lower()] == :
             index = index + 1
        dataCount[allword[index].lower()] = 1
        while index+ 1 < len(allword):
            if allword[index].lower() == allword[index+1].lower():
                dataCount[allword[i].lower()] += 1


    print(dataCount)
    print(allword)
    print(words)
    file.close()
def charCheck(input_char):
    # check letter
    if ((int(ord(input_char)) >= 65 and
         int(ord(input_char)) <= 90) or
            (int(ord(input_char)) >= 97 and
             int(ord(input_char)) <= 122)):
        return 1

    # check digit
    elif (int(ord(input_char)) >= 48 and
          int(ord(input_char)) <= 57):
        return 1

        # check special character
    else:
        return 0
getData('test.txt')
def count_score(score):
def sort_file():
def average_score():