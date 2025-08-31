import random
word_list = ["aardvark", "baboon", "camel"]
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.


print("start")
word = random.choice(word_list)

result = []
for i in range(0,len(word)):
    result.append("_")

print(word)
print("Begin")
count = 0
# index = 0
lives = 0
prev = 0

while lives<5:
    user_input = input("Choose a char").lower()
    index = 0

    for i in word:
        if i==user_input:
            result[index] = i
        index+=1

    curr = 0
    for i in result:
        if i =="_":
            curr+=1
    # print(f"{curr} current")
    # print(f"{prev} prev")
    if curr == len(word) or curr==prev:
        if (lives == 0):
            print(stages[5])
            lives+=1
        elif (lives == 1):
            print(stages[4])
            lives += 1
        elif (lives == 2):
            print(stages[3])
            lives += 1
        elif (lives == 3):
            print(stages[2])
            lives += 1
        elif (lives == 4):
            print(stages[1])
            lives += 1
        elif(lives == 4):
            print(stages[0])
            lives += 1

    if curr == 0:
        print("You win")
        break

    prev = curr
    count+=1
    print(result)
    # print(lives)

if lives ==5:
    print("You  loose")
print("Game Over")







