# Modularity and Records Assignment
# rubiks cube collection
# Program: Modularity & Records
# Name: Taha Sarfraz
#   Date: Sunday May 15th, 2022
# Description: This program accepts, sorts, and visualizes collectable rubiks
# cubes. User is given an entry field where they can type enter to enter information
# about the cube. User can type search to search for a specific rubiks cube using an
# entered name. Program will then list the list holding the cube. User can type draw,
# and is prompted to enter dimensions of cube. Program will then open tkinter and draw
# a 2d version of said cube. 
import array
import tkinter
from tkinter import *
import random

print("taha_mods.py\n")

print("Rubiks cube storage & collections.")
print("Enter cube information, search, modify, or draw 😎")

def record_vars(): # function for rubiks cube information collection (for records)
    cube_info = [0,0,0] # list that holds user inputted info
    cube_info[0] = input(f'{"Enter the name of the cube: ": >36}')
    cube_info[1]= input(f'{"Enter whether it is stickerless or not: ": >48}')
    cube_info[2] = input(f'{"Enter the dimensions of the cube (3x3, 4x4, etc): ": >58}')
    cube_info = str(cube_info)[1:-1] # converts list to string, and removes brackets
    return cube_info

def action(): # user action. user puts "enter, search, modify"
    user_action = input("Action: ")
    while (user_action != "enter" and user_action != "Enter" and user_action != "search" and user_action != "Search" and user_action != "modify" and user_action != "Modify" and user_action != "Draw" and user_action != "draw"): #above 79 characters, but making a list with the words didn't work have mercy.
        print(f'{"Invalid Input. Try again": >32}') #formatted string ensures clean code and follows 79 character convention
        user_action = input("Action: ") 
    if (user_action == "enter" or user_action == "Enter"):
        enter_action(1) #access the enter_action function. This starts the entry process
    if (user_action == "search" or user_action == "Search"):
        enter_action(2) # starts search process
        search_code() # function for searching program
    if (user_action == "modify" or user_action == "Modify"):
        enter_action(3) # modifying program
    if (user_action == "draw" or user_action == "Draw"):
        enter_action(4) # starts the drawing program
    return user_action #returns Action: prompt it to be used zd!

# search_code() splits all contents of text into lists, parses through the first
# object in each line, and compares the names with user inputted names in order
# to print the list containing the name the user wants.
#Currently, this code is not fully functioning. Code will only work is the name
# user enters is the same name as the final list in the code.
#so if you last type name = "john", and search for john, it will work.
# However, if you type name = 'cube', and search for john again, it won't work.
def search_code(): 
    file_in = 'cube.txt' 
    input_file = open (file_in, 'r') # sets the input .txt file as read
    cube_name = input(f'{"Enter name of cube - the list with the cube name will show: ": >68}')
    cube_name2 = "'" + cube_name + "'" + ","#ensures name is the same as it is stored in the string
    line_read = input_file.readline() #reads lines of the file
    samename = False #boolean var for storing whether or not matches have been found.
    while line_read != "":
        line_read = line_read.split() # parsing purposes
        if line_read[0] != cube_name2: # in slot 0, name is stored. 
            result_msg = 'no'           # program compares user's name to slot 0
            samename = False           # and prints the result
        if line_read[0] == cube_name2: # if a match is found
            result_msg = str(line_read[:])# program will print string of list
            samename = True
        line_read = input_file.readline ()
    if samename == True:
        print(str(result_msg)[2:-2] + ": name, stickers, dimensions") # prints formatted result message
    elif samename == False: #if no matches are made, prints formatted error msg
        print(f'{"No record found. Try again": >40}')
    line_read = input_file.readline ()
    input_file.close()
    
# when function is called, user gets to input information about the cube
# such as name, size, and stickered or stickerless.
def user_write(): 
    file_out = 'cube.txt'
    output_file = open(file_out, "a") # sets file to append in order to
                                      # add on user inputs without wiping
                                      # text file over and over again.
    print("Enter the manufacturer name, sticker variation, and the dimensions of your cube.")
    #record_vars()
    cube_information= record_vars() # allows the cube info to be printed
    print(cube_information) 
    output_file.write(str(cube_information) + "\n") #sends info to the file
                                                    #with formatted 
    output_file.close()

#this function organizes the use of different functions and allows the programmer to
# modify and tinker with functions without worrying about affection the function action()

# this also declutters the action and main function
# this also allows program to prompt user to input more actions. Without this function
# the prompt prompting user to enter, or draw would not show up.
def enter_action(num):
    # when called, user types a number to call specific actions from within function
    if (num == 1):
        user_write() # function for inputting cube information 
        action() # prompts user for further actions
    if (num == 2): 
        print("searching...")
        search_code() # function for searching code
        action() 
    if (num == 3):
        print(f'{"Access Denied. Contact your IT specialist. ": >51}') #formatted string
        action()
    if (num == 4):
        graphics() #function for drawing tkinter
        action()

#this function allows user to type in cube size, and then a window with a 2d model of the cube is
# drawn. User inputs a cube size (3x3), the first number would be read, and program would use that
# number to draw the cube using loops.
# Each box has a different color. 6 colors in total because a rubiks cube has 6 different colors on
# 6 sides. 

#Note; user stuuupid on stackoverflow helped in the making of this function. (not too much very little
# but they did help me)
def graphics():
    window = Tk()
    window.geometry("1920x1080")  # window dimensions
    # tile/window sizes
    tileSize = 100 # size for the box
    x = tileSize * 10 # controls size of the canvas
    y = tileSize * 10 # also controls the max size of the cube supported (currently 10x10)
                      # changeable by changing the * 10 to *12 to support (12x12) or smaller
    canvas = Canvas(window, bg='white', width=x, height=y)

    # cols = columns 
    cols = input(f'{"What size cube do you want? (3x3,2x2,...): ": >51}') 
    cols.split() #splits the user input's words as a single list
    cols = int(cols[0]) # reads the first object in the list
    rows = cols # and uses it for loops
    counter = 0 # for controlling random color scheme
    for col in range(cols): # runs as many times as user inputted number
        for row in range(rows): # runs as many times as user inputted number
            x = random.randint(1,6) #random number generator 1-6
            if (x == 1):
                cube_color = 'white'
            elif (x == 2):
                cube_color = 'red'
            elif (x == 3):
                cube_color = 'yellow'
            elif (x == 4):
                cube_color = 'green'
            elif (x == 5):
                cube_color = 'blue'
            elif (x == 6):
                cube_color = 'orange'
            counter += 1 
            canvas.create_rectangle(tileSize * col, tileSize * row, tileSize * col + tileSize, tileSize * row + tileSize, fill=cube_color, outline = 'black', width = 7)
            # on x axis, program draws one tile (tileSize), multiplied by size of cube (ex. 4x4, so tile is drawn
            # 4 times) but goes up by 100px each time
            # on y axis, program draws a tile (tileSize), multiplied by size of cube but goes right 100px each time.
    # Flips the shapes from memory onto the monitor
    canvas.pack()
    window.mainloop()
def main():
    action() #could be main 
    

main();


# the end !

