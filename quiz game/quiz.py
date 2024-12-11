print("##### welcome to my computer quiz #######")

playing = (input("would you like to play the quiz game? [y / n]")).upper()

if playing == 'Y':
    print("ok lets get started😊😊")
elif playing == "N":
    print("thank you for your time")
    quit()
else:
    print("you have entered the wrong key")

correct = 0
inCorrect = 0
questions = 5


q1 = input("what does cpu stands for:\n").upper()

if q1 == "CENTRAL PROCRSSING UNIT":
    print("you are correct!")
    correct += 1
else:
    print("your answer is incorrrect")
    inCorrect += 1

q2 = input("computer is a machine [true or false]\n").upper()

if q2 == "TRUE":
    print("you are correct!")
    correct += 1
else:
    print("your answer is incorrrect")
    inCorrect += 1

q3= input("computer programming is essential for everybody [true or false]\n").upper()

if q3 == "TRUE":
    print("you are correct!")
    correct += 1
else:
    print("your answer is incorrrect")
    inCorrect += 1

q4 = input("who is the first programmer?\n").upper()

if q4 == "Ada lovelence":
    print("you are correct!")
    correct += 1
else:
    print("your answer is incorrrect")
    inCorrect += 1

q5 = input("computer with out sw are nothing [true or false]\n").upper()

if q5 == "TRUE":
    print("you are correct!")
    correct += 1
else:
    print("your answer is incorrrect")
    inCorrect += 1

print(f'''

congratulation you have finished the quiz sucessfully🎉🎉🎉
============================================================
      | total number of questions => {questions}|         
      | correct answers => {correct}  |                   
      | incorrect answers => {inCorrect}|                   
============================================================      
''')
