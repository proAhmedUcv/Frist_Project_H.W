# import random as r



# gest_words=["ERP","Flwoer","Hamz"]

# choiceWord=r.choice(gest_words)
# Blankword=len(choiceWord)
# blank=[]
# temptry=3
# win=0
# for i in range(Blankword):
#     blank.append("_")
# print(choiceWord)
# for i in range(Blankword):
#     print(blank)
#     print(temptry)
#     enterLeter=input("Enter Leter...")
#     if enterLeter in choiceWord:
#         index=choiceWord.index(enterLeter)
#         blank[index]=enterLeter
#         win+=1
#         if win==len(blank):
#             print("win ..😎")
#             break
#     else:
#         temptry-=1
        
#         if temptry==0:
#             print("lose 😪")
#             break
#     # if index ==i:
#     #     blank[index]=enterLeter
    
#     # print(index)
#     # print(blank)
# # print(blank
# # print(blank) 


import random as r

guess_words = ["ERP", "Flower", "Hamz", "Python", "Programming", "OpenAI", "Game"]

play_again = True

while play_again:
    choiceWord = r.choice(guess_words)
    blank_word = len(choiceWord)
    blank = ["_" for _ in range(blank_word)]
    temp_try = 3
    win = 0

    print(choiceWord)

    while temp_try > 0:
        print(" ".join(blank))
        print(f"You have {temp_try} tries left.")
        enter_letter = input("Enter a letter...")

        if enter_letter in choiceWord:
            indices = [i for i, letter in enumerate(choiceWord) if letter == enter_letter]

            if len(indices) > 1:
                print("Multiple occurrences of the letter found!")
                index = int(input("Enter the position of the letter (1, 2, 3, ...): ")) - 1
                if index < 0 or index >= len(indices):
                    print("Invalid position. Try again.")
                    continue
            else:
                index = indices[0]

            blank[index] = enter_letter
            win += 1

            if win == len(blank):
                print("You win! 😎")
                break
        else:
            temp_try -= 1

            if temp_try == 0:
                print("You lose! 😪")
                break

    play_again_input = input("Do you want to play again? (Enter 1 for Yes, 0 for No): ")
    if play_again_input == "0":
        play_again = False
    elif play_again_input != "1":
        print("Invalid input. The game will continue.")

print("Thank you for playing!")
