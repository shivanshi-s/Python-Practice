import random
import string
print("H A N G M A N")
list_of_words = ('python', 'java', 'kotlin', 'javascript')
while 1:
    choose = input(f'Type "play" to play the game, "exit" to quit:')
    if choose == "play":

        right_answer = list(random.choice(list_of_words))
        user_answer = list("-" * len(right_answer))
        user_attempt = list()
        attempt = 8

        while attempt > 0:
            print("\n"+"".join(user_answer))
            letter = input(f"Input a letter: ")
            if len(letter) != 1:
                print("You should input a single letter")
            elif letter not in string.ascii_lowercase:
                print("Please enter a lowercase English letter")
            else:
                if letter in user_attempt:
                    print("You've already guessed this letter")
                elif letter not in right_answer:
                    attempt -= 1
                    print("That letter doesn't appear in the word")
                else:
                    index = 0
                    for _ in right_answer:
                        if right_answer[index] == letter:
                            user_answer[index] = letter
                        index += 1
                    if right_answer == user_answer:
                        print("""You guessed the word!\nYou survived!""")
                        break
            user_attempt.append(letter)
        else:
            print("You lost!")
    elif choose == "exit":
        break