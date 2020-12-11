
global probabilities
probabilities = []

class HuffmanCode:
    def __init__(self, probability):
        self.probability = probability

    def position(self, value, index):
        for j in range(len(self.probability)):
            if(value >= self.probability[j]):
                return j
        return index-1

    def compute_code(self):
        num = len(self.probability)
        huffman = ['']*num

        for i in range(num-2):
            val = self.probability[num-i-1] + self.probability[num-i-2]
            if(huffman[num-i-1] != '' and huffman[num-i-2] != ''):
                huffman[-1] = ['1' + symbol for symbol in huffman[-1]]
                huffman[-2] = ['0' + symbol for symbol in huffman[-2]]
            elif(huffman[num-i-1] != ''):
                huffman[num-i-2] = '0'
                huffman[-1] = ['1' + symbol for symbol in huffman[-1]]
            elif(huffman[num-i-2] != ''):
                huffman[num-i-1] = '1'
                huffman[-2] = ['0' + symbol for symbol in huffman[-2]]
            else:
                huffman[num-i-1] = '1'
                huffman[num-i-2] = '0'

            position = self.position(val, i)
            probability = self.probability[0:(len(self.probability) - 2)]
            probability.insert(position, val)
            if(isinstance(huffman[num-i-2], list) and isinstance(huffman[num-i-1], list)):
                complete_code = huffman[num-i-1] + huffman[num-i-2]
            elif(isinstance(huffman[num-i-2], list)):
                complete_code = huffman[num-i-2] + [huffman[num-i-1]]
            elif(isinstance(huffman[num-i-1], list)):
                complete_code = huffman[num-i-1] + [huffman[num-i-2]]
            else:
                complete_code = [huffman[num-i-2], huffman[num-i-1]]

            huffman = huffman[0:(len(huffman)-2)]
            huffman.insert(position, complete_code)

        huffman[0] = ['0' + symbol for symbol in huffman[0]]
        huffman[1] = ['1' + symbol for symbol in huffman[1]]

        if(len(huffman[1]) == 0):
            huffman[1] = '1'

        count = 0
        final_code = ['']*num

        for i in range(2):
            for j in range(len(huffman[i])):
                final_code[count] = huffman[i][j]
                count += 1

        final_code = sorted(final_code, key=len)
        return final_code

string = input("Enter the string to compute Huffman Code: ")

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
length = len(string)

probabilities = [float("{:.2f}".format(frequency[1]/length)) for frequency in freq]
probabilities = sorted(probabilities, reverse=True)

huffmanClassObject = HuffmanCode(probabilities)
P = probabilities

huffman = huffmanClassObject.compute_code()


for id,char in enumerate(freq):
    if huffman[id]=='':
        print(' %-4r |%12s' % (char[0], 1))
        continue
    print(' %-4r |%12s' % (char[0], huffman[id]))

