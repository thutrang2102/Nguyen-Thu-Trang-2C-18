

Question = ['1. Before backing up, you should ?',
            '2. It is best to keep a space cushion ?',
            '3. When no signs, signals, or police tell you what to do at an intersection, the law states that ?',
            '4. You must yield the right-of-way to an approaching vehicle when you are ?',
            '5. You have the right-of-way when you are ?']
Choice = ['A. Rely on your mirrors to see if it is clear to proceed\nB. Flash your lights\nC. Open your door to see if it is clear to proceed\nD. Turn your head and look through the rear wind',
          'C. A. Only in back of your vehicle\nB. Only on the left and right side of your vehicle\nC. Only in front of the vehicle\nD. On all sides of the vehicle',
          'A. Drivers on the right must yield to drivers on the left\nB. There are no laws stating who must yield\nC. Drivers going straight must yield to drivers turning left at the intersection\nD. Drivers turning left must yield to drivers going straight through the intersection',
          'A. Already in a traffic circle.\nB. Already in an intersection.\nC. Going straight ahead.\nD. Turning left.',
          'A. Entering a traffic circle.\nB. Backing out of a driveway.\nC. Leaving a parking space.\nD. Already in a traffic circle.']

Answer = ['A', 'C', 'A', 'A', 'D']
correct_answer = 0
wrong_answer = 0
for n in range(5):
    print(n+1, end='. ')
    print(Question[n])
    print(Choice[n])
    #Enter your answer
    student_answer = input('Your answer: ')
    for i in Answer:
      if student_answer == i:
         print('True')
         correct_answer += 1
         break
      else:
         print ('False')
         wrong_answer += 1
         break
print ('Correct answers: ', correct_answer)
print ('Wrong answers: ', wrong_answer)
# Condition
if correct_answer >= 3:
        print('Student passed the exam')
else:
        print('Student failed the exam')







