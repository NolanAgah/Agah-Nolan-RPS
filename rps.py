# file created by NOLAN AGAH
# import libraries

from time import sleep

from random import randint 

import pygame as pg

import os

game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 1000
HEIGHT = 600
FPS = 30

# colors
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# starts pygame - tells computer it's ready to use the pixels
pg.init()
# pygame tells tells the computer it's ready to use the speakers
pg.mixer.init()

# sets the size of the window for pygame to use
screen = pg.display.set_mode((WIDTH, HEIGHT))
# Sets the caption of the window to the string value
pg.display.set_caption("Rock, paper, scissors...")
# ticks the frames per second
clock = pg.time.Clock()

# stores the pixels of a file in a varible
rock_image = pg.image.load(os.path.join(game_folder, 'rockeyebrow.gif')).convert()
# stores dimensions and becomes mutable
rock_image_rect = rock_image.get_rect()
# set x coordinates for rock image
rock_image_rect.x = 650
# set y coordinates for rock image
rock_image_rect.y = 100

# see lines 39, 41, 43, and 45
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.png')).convert()
scissors_image_rect = scissors_image.get_rect()
scissors_image_rect.x = 350
scissors_image_rect.y = 450

# see lines 39, 41, 43, and 45
paper_image = pg.image.load(os.path.join(game_folder, 'paper.png')).convert()
paper_image_rect = paper_image.get_rect()
paper_image_rect.x = 50
paper_image_rect.y = 50

# creates a list of possible choices for cpu
rpslist = ["rock", "paper", "scissors"]

# sets the following conditions for the game true or false - start screen is true
playing = False
start_screen = True
choosing = False
rock_choice = False
scissors_choice = False
paper_choice = False
pc_choice = False
compare = False
results = False

# sets fonts used for the game
font = pg.font.SysFont(None, 48)
font2 = pg.font.SysFont(None, 32)

# defines function for cpu making their choice
def cpu_choose():
            # globals cpu_choice to be used for other functions outside of the function
            global cpu_choice
            # randomly chooses from rpslist
            cpu_choice = rpslist[randint(0,2)]
            # transforms function into a variable
            return cpu_choice

# calls the cpu_choose function
cpu_choose()

# initial game loop
while True:
    clock.tick(FPS)
    # runs for any event
    for event in pg.event.get():
        # if user clicks "x"
        if event.type == pg.QUIT:
            # pygame quits
            pg.quit()
            quit()
        # if the start screen is true, when user presses space, start screen is false and playing is true
        if start_screen:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    playing = True
                    start_screen = False
        # if rock choice is true, when user presses space, pc_choice is true while rock_choice is false
        elif rock_choice:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    pc_choice = True
                    rock_choice = False
        # if paper_choice is true, when user presses space, pc_choice is true while paper_choice is false
        elif paper_choice:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    pc_choice = True
                    paper_choice = False
        # if scissors_choice is true, when user presses space, pc_choice is true while scissors_choice is false
        elif scissors_choice:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    pc_choice = True
                    scissors_choice = False
        # if pc_choice is true, when user presses space, sets compare to true and pc_choice to false
        elif pc_choice:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    compare = True
                    pc_choice = False
    
    # fill the screen with black color
    screen.fill(BLACK)

    # if start screen is true
    if start_screen:
        # render the introductory text
        intro_text = font.render("Welcome to Rock, Paper, Scissors!", True, WHITE)
        # display the introductory text on the screen
        screen.blit(intro_text, (225, 270))
        # render the instruction to press space to advance
        intro_text2 = font2.render("Press space to advance...", True, WHITE)
        # display the instruction on the screen
        screen.blit(intro_text2, (375, 325))

    # if the game is in the playing state
    if playing:
        # display the images of rock, paper, and scissors on the screen
        screen.blit(rock_image, rock_image_rect)
        screen.blit(scissors_image, scissors_image_rect)
        screen.blit(paper_image, paper_image_rect)
        # if the player clicks the mouse button
        if event.type == pg.MOUSEBUTTONUP:
            # store the mouse position in a variable
            mouse_coords = pg.mouse.get_pos()
            # check which image the mouse has colided with
            if rock_image_rect.collidepoint(mouse_coords):
                rock_choice = True
                playing = False
                user_choice = "rock"
            elif paper_image_rect.collidepoint(mouse_coords):
                paper_choice = True
                playing = False
                user_choice = "paper"
            elif scissors_image_rect.collidepoint(mouse_coords):
                scissors_choice = True
                playing = False
                user_choice = "scissors"

    # if rock_choice is true
    if rock_choice:
        # display the rock image
        screen.blit(rock_image, rock_image_rect)
        # move the rock image
        rock_image_rect.x = 375
        rock_image_rect.y = 300
        # render the text that indicates the player has chosen rock
        rock_text = font2.render("You chose rock!", True, WHITE)
        # display the text on the screen
        screen.blit(rock_text, (375, 200))

    # if scissors_choice is true
    if scissors_choice:
        # display the scissors image
        screen.blit(scissors_image, scissors_image_rect)
        # move the scissors image
        scissors_image_rect.x = 375
        scissors_image_rect.y = 300
        # render the text that indicates the player has chosen scissors
        scissors_text = font2.render("You chose scissors!", True, WHITE)
        # display the text on the screen
        screen.blit(scissors_text, (375, 200))

    # if paper_choice is true
    if paper_choice:
        # display the paper image on screen
        screen.blit(paper_image, paper_image_rect)
        # move the paper image
        paper_image_rect.x = 375
        paper_image_rect.y = 300
        # render the text that indicates the player has chosen paper
        paper_text = font2.render("You chose paper!", True, WHITE)
        # display the text on the screen
        screen.blit(paper_text, (375, 200))

        
    # if paper_choice is true
    if paper_choice:
        # display the paper image on screen
        screen.blit(paper_image, paper_image_rect)
        # move the paper image
        paper_image_rect.x = 375
        paper_image_rect.y = 300
        # render the text that indicates the player has chosen paper
        paper_text = font2.render("You chose paper!", True, WHITE)
        # display the text on the screen
        screen.blit(paper_text, (375, 200))

    # if pc_choice is true
    if pc_choice:
        # check the value of cpu_choice and display the corresponding image and text
        if cpu_choice == "rock":
            screen.blit(rock_image, rock_image_rect)
            rock_image_rect.x = 375
            rock_image_rect.y = 300
            cpu_rock_text = font2.render("Computer chose rock!", True, WHITE)
            screen.blit(cpu_rock_text, (375, 200))
        elif cpu_choice == "scissors":
            screen.blit(scissors_image, scissors_image_rect)
            scissors_image_rect.x = 375
            scissors_image_rect.y = 300
            cpu_scissors_text = font2.render("Computer chose scissors!", True, WHITE)
            screen.blit(cpu_scissors_text, (375, 200))
        elif cpu_choice == "paper":
            screen.blit(paper_image, paper_image_rect)
            paper_image_rect.x = 375
            paper_image_rect.y = 300
            cpu_paper_text = font2.render("Computer chose paper!", True, WHITE)
            screen.blit(cpu_paper_text, (375, 200))

    # if compare is true
    if compare:
        # check the values of user_choice and cpu_choice to determine the outcome of the game
        # tie condition
        if user_choice == cpu_choice:
            tie_text = font2.render("It's a tie!", True, WHITE)
            screen.blit(tie_text, (425, 200))
        # rock beats paper win condition
        elif user_choice == "rock" and cpu_choice == "scissors":
            win_text = font2.render("You win!", True, WHITE)
            screen.blit(win_text, (425, 200))
        # scissors beats paper win condition
        elif user_choice == "scissors" and cpu_choice == "paper":
            win_text = font2.render("You win!", True, WHITE)
            screen.blit(win_text, (425, 200))
        # paper beats rock win condition
        elif user_choice == "paper" and cpu_choice == "rock":
            win_text = font2.render("You win!", True, WHITE)
            screen.blit(win_text, (425, 200))
        # rock loses to paper loss condition
        elif user_choice == "rock" and cpu_choice == "paper":
            lose_text = font2.render("You lose!", True, WHITE)
            screen.blit(lose_text, (425, 200))
        # paper loses to scissors loss condition
        elif user_choice == "paper" and cpu_choice == "scissors":
            lose_text = font2.render("You lose!", True, WHITE)
            screen.blit(lose_text, (425, 200))
        # scissors loses to rock loss condition
        elif user_choice == "scissors" and cpu_choice == "rock":
            lose_text = font2.render("You lose!", True, WHITE)
            screen.blit(lose_text, (425, 200))

    pg.display.flip()

pg.quit()