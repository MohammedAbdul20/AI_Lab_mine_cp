import random
from hangman_words import word_list
from hangman_art import stages,logo
chosen_word=random.choice(word_list)
lives=len(chosen_word)
print(f'pssst, the solution is {chosen_word}')
print(logo)
display=[]
for i in range(len(chosen_word)):
      display.append("_")
while "_" in display:
      guess=input("guess a letter:").lower()
      for i in range(len(chosen_word)):
            letter=chosen_word[i]
            if letter==guess:
                  if display[i]==letter:
                        print('repeated')
                  else:
                        display[i]=letter
      if guess not in chosen_word:
            lives=lives-1
            if lives==0:
                  print("you lose")
                  exit(1)
      print(f"{' '.join(display)}")
      print(stages[lives])
else:
      print("you have won")
