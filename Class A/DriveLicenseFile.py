
exam_question = open('Question.txt', 'r')
exam_choice = open('Choice.txt', 'r')

Answer = ['A', 'C', 'A', 'A', 'D']
correct_answer = 0
wrong_answer = 0
for n in range(5):
    Q = exam_question.readline()
    print(n+1, end='. ')
    print(exam_question[n])
    C = exam_choice.readline()
    C = C.rstrip('\n')
    print(exam_choice[n])
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
print('Correct answers: ', correct_answer)
print('Wrong answers: ', wrong_answer)
# Condition
if correct_answer >= 3:
        print('Student passed the exam')
else:
        print('Student failed the exam')

exam_question.close()
exam_choice.close()





