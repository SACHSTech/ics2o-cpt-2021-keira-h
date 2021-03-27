""" 
A basic pygame template
"""
 
import pygame

#---------------------------------------
# Define some colors
BLACK       = (   0,   0,   0)
WHITE       = ( 255, 255, 255)
GREEN       = (   0, 255,   0)
RED         = ( 255,   0,   0)
LIGHT_BEIGE = ( 245, 241, 234)
BEIGE       = ( 236, 232, 223)
DARK_BEIGE  = ( 208, 201, 190)
BLUE_GREY   = ( 151, 162, 167)
SLATE_GREY  = ( 111, 116, 134)
DARK_GREEN  = ( 140, 144, 134)

# Initialize pygame
pygame.init()

# Set the width and height of the screen [width, height]
display_width  = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
 
pygame.display.set_caption("<insert title>")
#---------------------------------------
# ------------- Buttons -------------
# Start Button 
startbutton_x = 440
startbutton_y = 275
startbutton_width = 275
startbutton_height = 140

# Help Buttons
helpbutton_x = 90
helpbutton_y = 275
helpbutton_width = 275
helpbutton_height = 140

# Return Home Button
returnbutton_x = 0
returnbutton_y = 0
returnbutton_width = 200
returnbutton_height = 35

# Option 1
option1_x = 110
option1_y = 455
option1_width = 580
option1_height = 50

# Option 2
option2_x = 110
option2_y = 530
option2_width = 580
option2_height = 50

# Bring To Next Scene 
nextscene1_x = 220
nextscene1_y = 480
nextscene1_width = 360
nextscene1_height = 75

# Bring To Next Scene (Second Button)
nextscene2_x = 220
nextscene2_y = 480
nextscene2_width = 360
nextscene2_height = 75

button_pressed = False
mouse_click_position = [0,0]
q_click_position = [0,0]
#---------------------------------------
# --------------- Boxes ---------------
# Help Box 
helpbox_x = 100
helpbox_y = 90
helpbox_width = 630
helpbox_height = 450

# Text Box
textbox_x = 100
textbox_y = 425
textbox_width = 600
textbox_height = 175
#---------------------------------------
# --------------- Images ---------------
# Starting Page Images
test = pygame.image.load("test.jpg")
test = pygame.transform.smoothscale(test, (350, 250))

# Scene 1 Images
dog = pygame.image.load("dog.JPG")
dog = pygame.transform.smoothscale(dog, (500,300))

test2 = pygame.image.load("other.png")
test2 = pygame.transform.smoothscale(test2, (350, 250))
#---------------------------------------
# ----------- Fonts and Text -----------
# Fonts  
fonttitle1 = pygame.font.SysFont("freesans",70,bold=True)
font2 = pygame.font.SysFont("freesans",50,bold=True)
font3 = pygame.font.SysFont("freesans",30,bold=True)
font4 = pygame.font.SysFont("freesans",20,bold=True)
font5 = pygame.font.SysFont("freesans",20,bold=True,italic=True)
#---------------------------------------
# Text (Starting Page)
title1 = fonttitle1.render("<insert title>", True, (BLACK))
header1 = font2.render("START", True, (BLACK))
header2 = font2.render("HELP", True, (BLACK))
#---------------------------------------
# Text (Help Page) 
header3 = font2.render("About the Game", True, (WHITE))
text1 = font4.render("You are planning to build your own computer! For many months,", True, (WHITE))
text1_1 = font4.render("you have been saving up your money for this day. You decided", True, (WHITE))
text1_2 = font4.render("to buy the hardware components after your job since today was", True, (WHITE))
text1_3 = font4.render("payday(You gotta have that extra money ;)).", True, (WHITE))
text1_4 = font4.render("Use \"Q\" to continue through the dialogue.", True, (WHITE))
returntext = font3.render("Return Home", True, (WHITE)) 

header3_1 = font2.render("Word of Advice", True, (WHITE))
text2 = font4.render("<insert title> is a decision-based game, where your choices will", True, (WHITE))
text2_1 = font4.render("reflect your outcome result. Spend your money and choose your", True, (WHITE))
text2_2 = font4.render("choices wisely. You never know what consequences may occur...", True, (WHITE))
#---------------------------------------
# Text Titles
usertext = font3.render("User", True, (WHITE))
usertext_rect = usertext.get_rect()
usertext_x = screen.get_width() / 2 - usertext_rect.width / 2

bosstext = font3.render("Boss", True, (WHITE))
bosstext_rect = bosstext.get_rect()
bosstext_x = screen.get_width() / 2 - bosstext_rect.width / 2
#---------------------------------------
# Text Dialogue (Scene 1)
dialogue1_1 = font4.render("Ahhh. Today is payday! I will finally have enough money to", True, (WHITE))
dialogue1_2 = font4.render("build my computer. I better finish up quickly.", True, (WHITE))
dialogue1_3 = font5.render("Few hours later", True, (WHITE))
dialogue1_4 = font4.render("FINALLY! I better see the boss ot collect my paycheck.", True, (WHITE))
dialogue2_1 = font4.render("Ahhh, there you are. I was wondering if you're", True, (WHITE))
dialogue2_2 = font4.render("willing to do a few more extra tasks before leaving", True, (WHITE))
#---------------------------------------
# Option 1 (Scene 1)
option1_1 = font4.render("Sure, I don’t have anything else to do.", True, (WHITE))
optdialogue1_1 = font4.render("Thank you so much! I’ll pay you more for overtime!", True, (WHITE))
optdialogue1_2 = font5.render("-- USER RECEIVES $450 --", True, (WHITE))
#---------------------------------------
# Option 2 (Scene 1)
option1_2 = font4.render("Sorry, I need to do something right after this.", True, (WHITE))
optdialogue2_1 = font4.render("Oh, ok then, I’ll just give you your paycheck for this month", True, (WHITE))
optdialogue2_2 = font5.render("-- USER RECEIVES $250 --", True, (WHITE))
banktext = font2.render("GO TO BANK", True, (WHITE))
#---------------------------------------
# Text Dialogue (Scene 2)
dialogue3_1 = font4.render("Alright. I'm going to deposit some money and see how much", True, (WHITE))
dialogue3_2 = font4.render("I have now.", True, (WHITE))
money_amt1 = font5.render("AMOUNT OF MONEY = $2450.00", True, (WHITE))
money_amt2 = font5.render("AMOUNT OF MONEY = $2250.00", True, (WHITE))
dialogue3_3 = font4.render("Now that's done, I'm going to go to the hardware store.", True, (WHITE))
#---------------------------------------
# Load next scene
scene = 1

#Loop until the user clicks the close button.
done = False
show_text = 1
show_text1 = 1
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print("Continue")
                q_click_position = pygame.key.get_pressed()
                show_text += 1
                show_text1 += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
          print("User pressed a mouse button.")
          mouse_click_position = pygame.mouse.get_pos()

    # Start Page 
    if scene == 1:
      # Fill background
      screen.fill(LIGHT_BEIGE)

      # Input images and/or text
      screen.blit(dog,(0,0))
      screen.blit(title1,(100,100))

      # Drawing Button
      pygame.draw.rect(screen, RED, [startbutton_x, startbutton_y, startbutton_width, startbutton_height])
      pygame.draw.rect(screen, GREEN, [helpbutton_x, helpbutton_y, helpbutton_width, helpbutton_height])
      
      # Checking Button
      if (startbutton_x <= mouse_click_position[0] and mouse_click_position[0] <= startbutton_x + startbutton_width) and (startbutton_y <= mouse_click_position[1] and mouse_click_position[1] <= startbutton_y + startbutton_height):
          scene = 3
      elif (helpbutton_x <= mouse_click_position[0] and mouse_click_position[0] <= helpbutton_x + helpbutton_width) and (helpbutton_y <= mouse_click_position[1] and mouse_click_position[1] <= helpbutton_y + helpbutton_height):
          scene = 2
      
      # Text
      screen.blit(header1,(500,325))
      screen.blit(header2,(160,325))

    # Help Page
    elif scene == 2:
      # Fill background
      screen.fill(DARK_BEIGE)

      # Text Box
      pygame.draw.rect(screen, BLACK,[helpbox_x, helpbox_y, helpbox_width, helpbox_height])

      # Input images and/or text
      screen.blit(header3,(225,100))
      screen.blit(text1,(105,150))
      screen.blit(text1_1,(105,175))
      screen.blit(text1_2,(105,200))
      screen.blit(text1_3,(105,225))
      screen.blit(text1_4,(105,250))

      screen.blit(header3_1,(225,325))
      screen.blit(text2,(105,375))
      screen.blit(text2_1,(105,400))
      screen.blit(text2_2,(105,425))

      # Draw Button
      pygame.draw.rect(screen, SLATE_GREY, [returnbutton_x, returnbutton_y, returnbutton_width, returnbutton_height])
      screen.blit(returntext,(3,3))

      # Check Button
      if (returnbutton_x <= mouse_click_position[0] and mouse_click_position[0] <= returnbutton_x + returnbutton_width) and (returnbutton_y <= mouse_click_position[1] and mouse_click_position[1] <= returnbutton_y + returnbutton_height):
          scene = 1

    # Scene 1
    elif scene == 3:
      # Fill background
      screen.fill(DARK_BEIGE)

      # Text Box
      pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])

      # Input images
      screen.blit(test2,(0,0)) 
      
      # Show dialogue
      if show_text == 1:
        screen.blit(usertext, [usertext_x, 425])
        screen.blit(dialogue1_1,(110,460))
        screen.blit(dialogue1_2,(110,480)) 
      elif show_text == 2:
        screen.blit(dialogue1_3,(110,460))
      elif show_text == 3:
        screen.blit(usertext,(355,425))
        screen.blit(dialogue1_4,(110,460))
      elif show_text == 4:
        screen.blit(bosstext, [bosstext_x, 425]) 
        screen.blit(dialogue2_1,(110,460))
        screen.blit(dialogue2_2,(110,482))
      
      # Provide options
      else:
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(option1_1,(120,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(option1_2,(120,545)) 
      
      # Check Buttons
      if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
          scene = 4
      if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
          scene = 5

    # Option 1  
    elif scene == 4:
      # Fill background
      screen.fill(BLUE_GREY)
      
      # Text Box
      pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])

      if show_text1 == 5:
        # Input images and/or text
        screen.blit(bosstext, [bosstext_x, 425])
        screen.blit(optdialogue1_1,(110,460))
        screen.blit(optdialogue1_2,(110,485))

      else:
        # Draw Button (with Text)
        pygame.draw.rect(screen, SLATE_GREY, [nextscene1_x, nextscene1_y, nextscene1_width, nextscene1_height])
        screen.blit(banktext,(240,495))

        # Check Button
        if (nextscene1_x <= mouse_click_position[0] and mouse_click_position[0] <= nextscene1_x + nextscene1_width) and (nextscene1_y <= mouse_click_position[1] and mouse_click_position[1] <= nextscene1_y + nextscene1_height):
          scene = 6 

    # Option 2
    elif scene == 5:
      # Fill background
      screen.fill(BLUE_GREY)
      
      # Text Box
      pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])

      if show_text1 == 5:
        # Input images and/or text
        screen.blit(bosstext, [bosstext_x, 425])
        screen.blit(optdialogue2_1,(110,485))
        screen.blit(optdialogue2_2,(110,460))

      else:
        # Draw Button (with Text)
        pygame.draw.rect(screen, SLATE_GREY, [nextscene1_x, nextscene1_y, nextscene1_width, nextscene1_height])
        screen.blit(banktext,(240,495))

        # Check Button 
        if (nextscene1_x <= mouse_click_position[0] and mouse_click_position[0] <= nextscene1_x + nextscene1_width) and (nextscene1_y <= mouse_click_position[1] and mouse_click_position[1] <= nextscene1_y + nextscene1_height):
          scene = 7
    
    # Scene 2 (Option 1 Path)
    elif scene == 6:
      # Fill background
      screen.fill(BEIGE)

      # Text Box
      pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])

      # Input images
      
      
      # Show dialogue
      if show_text == 6:
        screen.blit(usertext, [usertext_x, 425])
        screen.blit(dialogue3_1,(110,460))
        screen.blit(dialogue3_2,(110,480)) 
      elif show_text == 7: 
        screen.blit(money_amt1,(110,460))
      else:
        screen.blit(usertext, [usertext_x, 425])
        screen.blit(dialogue3_3,(110,460))
    
    # Scene 2 (Option 2 Path)
    elif scene == 7:
      # Fill background
      screen.fill(BEIGE)

      # Text Box
      pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])

      # Input images
      
      
      # Show dialogue
      if show_text == 6:
        screen.blit(usertext, [usertext_x, 425])
        screen.blit(dialogue3_1,(110,460))
        screen.blit(dialogue3_2,(110,480)) 
      elif show_text == 7: 
        screen.blit(money_amt2,(110,460))
      else:
        screen.blit(usertext, [usertext_x, 425])
        screen.blit(dialogue3_3,(110,460))

    else:
      screen.fill(BEIGE)

        
      
      
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()