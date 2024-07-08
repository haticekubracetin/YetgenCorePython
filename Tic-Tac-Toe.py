player1 = input("First player's name (X): ")
player2 = input("Second player's name (O): ")
counter = 0

row1 =  [' ', ' ', ' '] # 1, 2, 3 
row2 =  [' ', ' ', ' '] # 4, 5, 6
row3 =  [' ', ' ', ' '] # 7, 8, 9

def printTable():
    print(row1)
    print(row2)
    print(row3)

def choice():
    global counter
    decision = input("Please select a number between 1 and 9. (both included)")
    while not decision.isdigit():
        print("It's not a digit. Please try a number between 1 and 9.")
        decision = input("Please select a number between 1 and 9. (both included)")
    decision = int(decision)
    while decision not in range(1,10):
        print("Please try a number between 1 and 9.")
        decision = input("Please select a number between 1 and 9. (both included)")
    counter+=1
    return decision

def writeToTable(decision, letter):
    global counter
    if decision in range(1,4):
        decision = decision - 1
        if row1[decision] == " ":
            row1[decision] = letter
        else:
            counter-=1
            print("This position has already been filled. Please try another position.")
    elif decision in range(4,7):
        decision = (decision-1) % 3
        if row2[decision] == " ":
            row2[decision] = letter
        else:
            counter-=1
            print("This position has already been filled. Please try another position.")
    elif decision in range(7,10):
        decision = (decision-1) % 3
        if row3[decision] == " ":
            row3[decision] = letter
        else:
            counter-=1
            print("This position has already been filled. Please try another position.")
    else:
        print("Invalid choice. Please restart the game.")
    printTable()

def isGameOver():
    global player1, player2
    winner = ""
    if counter % 2 == 0:
        winner = player2
    else:
        winner = player1
    
    if row1[0]==row2[0]==row3[0]=="X" or row1[1]==row2[1]==row3[1]=='X' or row1[2]==row2[2]==row3[2]=='X' or row1[0]==row1[1]==row1[2]=='X' or row2[0]==row2[1]==row2[2]=='X' or row3[0]==row3[1]==row3[2]=='X' or row1[0]==row2[0]==row3[0]=="O" or row1[1]==row2[1]==row3[1]=='O' or row1[2]==row2[2]==row3[2]=='O' or row1[0]==row1[1]==row1[2]=='O' or row2[0]==row2[1]==row2[2]=='O' or row3[0]==row3[1]==row3[2]=='O' or row1[0]==row2[1]==row3[2]=="X" or row1[2]==row2[1]==row3[0]=="X" or row1[0]==row2[1]==row3[2]=="O" or row1[2]==row2[1]==row3[0]=="O":
        print('Game over! Congratulations, {}'.format(winner))
        return True
    else:
        return False

while not isGameOver():
    letter = ''
    if counter % 2 == 0:
        print("It's your turn: ", player1)
        letter = 'X'
    else:
        print("It's your turn: ", player2)
        letter = 'O'
    decision = choice()
    writeToTable(decision,letter)
