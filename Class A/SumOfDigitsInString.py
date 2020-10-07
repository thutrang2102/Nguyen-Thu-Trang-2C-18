
number_string = input('Enter a series of single digit number:')
sum = 0
for i in number_string:
    if i.isdigit():
       sum += int(i)
print('\nThe sum of all the single  digit numbers in the string', number_string,'is',str(sum))