import random
from os import system
import time
system("cls")
list_colors=["Blue","Green","Red","Yellow"]
chosen_colors=[]
color_input_control=1
index_control=0
color_count=0
print("Welcome to Color Game. You have to repeat the colors in order without breaking the sequence.\nA new color will be added to the list with each round. Good Luck!\nWrite 'S' to start the game or 'Q' to Quit.")
game_control=input("Start or Quit?")
while game_control!="S" and game_control!="Q":
    game_control=input("Start or Quit?")
def taking_color():
    global color_count
    global index_control
    if len(chosen_colors)>=1:
        for i in range(0,len(chosen_colors)):
            time.sleep(1)
            system("cls")
            time.sleep(1)
            print(chosen_colors[i])
            time.sleep(1)    
    system("cls")
    color=random.choice(list_colors)
    chosen_colors.append(color)
    time.sleep(1)
    print(color)
    time.sleep(1)
    system("cls")
    time.sleep(1)
    color_count+=1
    index_control=0
while color_count<=len(chosen_colors):
    if game_control=="Q":
        break
    if color_input_control==1:
            taking_color()
    else:
        break
    if len(chosen_colors)==color_count:
        while color_input_control==1:
            if index_control==len(chosen_colors):
                print(random.choice(["Well Done!","Perfect!","So Good!","Wonderful!"]))
                break
            color_entry=input("Entry Color: ")
            if color_entry==chosen_colors[index_control]:
                index_control+=1
            else:
                color_input_control=0
                print("You Lose.")
                break