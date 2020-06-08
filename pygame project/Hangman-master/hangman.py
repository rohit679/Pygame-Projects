import pygame
import random

pygame.init()
winHeight = 480
winWidth = 700
win=pygame.display.set_mode((winWidth,winHeight))  #setting the gaming window
#---------------------------------------#
# initialize global variables/constants #
#---------------------------------------#
BLACK = (0,0, 0)  #setting all the colors
WHITE = (255,255,255)
RED = (255,0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BLUE = (102,255,255)

btn_font = pygame.font.SysFont("arial", 20)  #stting button text font
guess_font = pygame.font.SysFont("monospace", 24) #setting guess text font
lost_font = pygame.font.SysFont('arial', 45)  #setting the game over message font
word = ''  #string to store the word
buttons = []  #list to store buttons
guessed = []  #list of guessed letters

#storing all the images of hangman
hangmanPics = [pygame.image.load('hangman0.png'), pygame.image.load('hangman1.png'), pygame.image.load('hangman2.png'), pygame.image.load('hangman3.png'), pygame.image.load('hangman4.png'), pygame.image.load('hangman5.png'), pygame.image.load('hangman6.png')]

limbs = 0  #variable to store the number of wrong guess


def redraw_game_window():
    global guessed
    global hangmanPics
    global limbs
    win.fill(GREEN)
    # Buttons
    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(win, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])  #drawing the button circles
            pygame.draw.circle(win, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2)
            label = btn_font.render(chr(buttons[i][5]), 1, BLACK)  #storing the character into label that we want to draw
            win.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2))) #printing the letter into the screen

    spaced = spacedOut(word, guessed)  #passing word and guessed list into the function for checking,it's right or not
    label1 = guess_font.render(spaced, 1, BLACK)
    rect = label1.get_rect()
    length = rect[2]
    
    win.blit(label1,(winWidth/2 - length/2, 400))

    pic = hangmanPics[limbs]  #loading each pick depending upon the limb
    win.blit(pic, (winWidth/2 - pic.get_width()/2 + 20, 150))  #show the respective pic into the screen
    pygame.display.update()


def randomWord():  #function for choosing any word from word.txt
    file = open('words.txt')
    f = file.readlines()
    i = random.randrange(0, len(f) - 1)

    return f[i][:-1]


def hang(guess):  #function that will define whether the guessed letter is correct or not
    global word
    if guess.lower() not in word.lower():  #lower function is used to convert capital letters to small letters
        return True
    else:
        return False


def spacedOut(word, guessed=[]):  #if the guessed letter is in our word then we need to remove that button
    spacedWord = ''
    guessedLetters = guessed
    for x in range(len(word)):
        if word[x] != ' ':
            spacedWord += '_ '
            for i in range(len(guessedLetters)):
                if word[x].upper() == guessedLetters[i]:
                    spacedWord = spacedWord[:-2]
                    spacedWord += word[x].upper() + ' '
        elif word[x] == ' ':
            spacedWord += ' '
    return spacedWord
            

def buttonHit(x, y):  #checking for letter where the button has been pressed
    for i in range(len(buttons)):
        if x < buttons[i][1] + 20 and x > buttons[i][1] - 20:
            if y < buttons[i][2] + 20 and y > buttons[i][2] - 20:
                return buttons[i][5]
    return None


def end(winner=False):  #end function will be called when the game is going to over
    global limbs
    lostTxt = 'You Lost, press any key to play again...'
    winTxt = 'WINNER!, press any key to play again...'
    redraw_game_window()  #calling function that we made for redrawing the window
    pygame.time.delay(1000)
    win.fill(GREEN)

    if winner == True:  #if win then print the winning text onto the screen else print loosing text
        label = lost_font.render(winTxt, 1, BLACK)
    else:
        label = lost_font.render(lostTxt, 1, BLACK)

    wordTxt = lost_font.render(word.upper(), 1, BLACK)  #loading the word that was the answer
    wordWas = lost_font.render('The phrase was: ', 1, BLACK)  #loading the phrase

    win.blit(wordTxt, (winWidth/2 - wordTxt.get_width()/2, 295))  #printing the real answer
    win.blit(wordWas, (winWidth/2 - wordWas.get_width()/2, 245))  #printing the phrase
    win.blit(label, (winWidth / 2 - label.get_width() / 2, 140))  #printing the winning or loosing message
    pygame.display.update()
    
    again = True  #for reset the game we require user input so following output is for that halt
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                again = False
    reset()


def reset():  #function to reset the game
    global limbs
    global guessed
    global buttons
    global word
    for i in range(len(buttons)):
        buttons[i][4] = True

    limbs = 0
    guessed = []
    word = randomWord()

#MAINLINE


# Setup button position of 26 letters
increase = round(winWidth / 13)
for i in range(26):
    if i < 13:
        y = 40
        x = 25 + (increase * i)
    else:
        x = 25 + (increase * (i - 13))
        y = 85
    buttons.append([LIGHT_BLUE, x, y, 20, True, 65 + i])
    # buttons.append([color, x_pos, y_pos, radius, visible, char])

word = randomWord()  #calling function that we made for choosing the word randomly
inPlay = True

while inPlay:
    redraw_game_window()  #calling the function that we made
    pygame.time.delay(10)  #setting the delay

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #handling the quit event, when the user close the window
            inPlay = False
        if event.type == pygame.KEYDOWN:  #or the user presses the escape
            if event.key == pygame.K_ESCAPE:
                inPlay = False
        if event.type == pygame.MOUSEBUTTONDOWN: #checking condition when the mouse is being pressed into the screen
            clickPos = pygame.mouse.get_pos()  #getting the pressed position into a variable
            letter = buttonHit(clickPos[0], clickPos[1])  #calling the function by passing the pressed position for knowing which button is being pressed
            #which return the respective button, which will be stored into the letter
            if letter != None:  #if there exixt any letter
                guessed.append(chr(letter))  #append that letter into guessed list
                buttons[letter - 65][4] = False
                if hang(chr(letter)):  #if function return true,which means guess was not correct
                    if limbs != 5:  #checking if limb is not equal to 5 then increase it else call end function for game over
                        limbs += 1
                    else:
                        end()
                else:  #if hang function return false then else will execute where we call spaceout function for making blank space
                    print(spacedOut(word, guessed))
                    if spacedOut(word, guessed).count('_') == 0:
                        end(True)

pygame.quit()

# always quit pygame when done!
