#v2.1
import random
from os import system
import time
from termcolor import colored
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
            if chosen_colors[i]=="Red":
                print(colored (chosen_colors[i],"red"))
            if chosen_colors[i]=="Green":
                print(colored (chosen_colors[i],"green"))
            if chosen_colors[i]=="Blue":
                print(colored (chosen_colors[i],"blue"))
            if chosen_colors[i]=="Yellow":
                print(colored (chosen_colors[i],"yellow"))
            time.sleep(1)    
    system("cls")
    color=random.choice(list_colors)
    chosen_colors.append(color)
    time.sleep(1)
    if chosen_colors[-1]=="Red":
        print(colored ("Red","red"))
    if chosen_colors[-1]=="Green":
        print(colored ("Green","green"))
    if chosen_colors[-1]=="Blue":
        print(colored ("Blue","blue"))
    if chosen_colors[-1]=="Yellow":
        print(colored ("Yellow","yellow"))
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
            color_entry=input("Enter Color: ")
            if color_entry==chosen_colors[index_control]:
                index_control+=1
                if color_entry=="Red":
                    print ("\033[A                             \033[A")
                    print("Enter Color:"+" "+colored("Red","red"))
                if color_entry=="Green":
                    print ("\033[A                             \033[A")
                    print("Enter Color:"+" "+colored("Green","green"))
                if color_entry=="Blue":
                    print ("\033[A                             \033[A")
                    print("Enter Color:"+" "+colored("Blue","blue"))
                if color_entry=="Yellow":
                    print ("\033[A                             \033[A")
                    print("Enter Color:"+" "+colored("Yellow","yellow"))
            else:
                if color_entry=="Blue":
                    print ("\033[A                             \033[A")
                    wrong_color=colored("Blue","blue")
                    print(f"Enter Color: {wrong_color}")
                if color_entry=="Green":
                    print ("\033[A                             \033[A")
                    wrong_color=colored("Green","green")
                    print(f"Enter Color: {wrong_color}")
                if color_entry=="Red":
                    print ("\033[A                             \033[A")
                    wrong_color=colored("Red","red")
                    print(f"Enter Color: {wrong_color}")
                if color_entry=="Yellow":
                    print ("\033[A                             \033[A")
                    wrong_color=colored("Yellow","yellow")
                    print(f"Enter Color: {wrong_color}")                   
                color_input_control=0
                if chosen_colors[index_control]=="Blue":
                    correct_color=colored(chosen_colors[index_control],"blue")
                    print(f"You Lose. {correct_color} was correct.")
                if chosen_colors[index_control]=="Green":
                    correct_color=colored(chosen_colors[index_control],"green")
                    print(f"You Lose. {correct_color} was correct.")
                if chosen_colors[index_control]=="Red":
                    correct_color=colored(chosen_colors[index_control],"red")
                    print(f"You Lose. {correct_color} was correct.")
                if chosen_colors[index_control]=="Yellow":
                    correct_color=colored(chosen_colors[index_control],"yellow")
                    print(f"You lose. {correct_color} was correct.")
                break