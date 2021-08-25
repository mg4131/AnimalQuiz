def checkguess(guess, answer):
  global score
  stillguessing=True
  attempt=0
  while stillguessing==True and attempt < 3:
    if guess.upper() == answer.upper():
      print('Correct')
      score+=1
      stillguessing=False
    else:
      if attempt < 2:
        guess = input('Sorry, Wrong answer. Try again. ')
      attempt += 1
  if attempt == 3:
    print('The correct answer is ' + answer + '!')
score=0
print('Guess the Animal')
guess1=input('Which bear lives at the North Pole: ')
checkguess(guess1, 'POLAR BEAR')
guess2=input('Which is the fastest land animal: ')
checkguess(guess2, 'CHEETAH')
guess3=input('Which is the largest animal: ')
checkguess(guess3, 'BLUE WHALE')
print('Your score is ' + str(score))
