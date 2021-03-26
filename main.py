""" 
A basic pygame template
"""
 
import pygame
 
# Define some colors
BLACK      = (   0,   0,   0)
WHITE      = ( 255, 255, 255)
GREEN      = (   0, 255,   0)
RED        = ( 255,   0,   0)
BEIGE      = ( 245, 241, 234)
DARK_BEIGE = ( 208, 201, 190)
BLUE_GREY  = ( 151, 162, 167)

pygame.init()
  
# Set the width and height of the screen [width, height]
display_width  = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
 
pygame.display.set_caption("<insert title>")
 
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
returnbutton_width = 154
returnbutton_height = 35

# Option 1
button1_x = 167
button1_y = 96
button1_width = 154
button1_height = 35

button_pressed = False
mouse_click_position = [0,0]
q_click_position = [0,0]


# --------- Images and Texts ---------
# ⋯⋯⋯⋯⋯⋯⋯ Starting Page Images ⋯⋯⋯⋯⋯⋯⋯
test = pygame.image.load("test.jpg")
test = pygame.transform.smoothscale(test, (350, 250))

# ⋯⋯⋯⋯⋯⋯⋯⋯ Scene 1 Images ⋯⋯⋯⋯⋯⋯⋯⋯
dog = pygame.image.load("dog.JPG")
dog = pygame.transform.smoothscale(dog, (500,300))

test2 = pygame.image.load("other.png")
test2 = pygame.transform.smoothscale(test2, (350, 250))

# ⋯⋯⋯⋯⋯⋯⋯⋯ Fonts ⋯⋯⋯⋯⋯⋯⋯⋯ 
fonttitle1 = pygame.font.SysFont("freesans",70,bold=True)
font2 = pygame.font.SysFont("freesans",50,bold=True)
font3 = pygame.font.SysFont("freesans",30,bold=True)
font4 = pygame.font.SysFont("freesans",20,bold=True)

# ⋯⋯⋯⋯⋯⋯⋯ Text (Starting Page) ⋯⋯⋯⋯⋯⋯⋯
title1 = fonttitle1.render("<insert title>", True, (BLACK))
header1 = font2.render("START", True, (BLACK))
header2 = font2.render("HELP", True, (BLACK))

# ⋯⋯⋯⋯⋯⋯⋯⋯ Text (Help Page) ⋯⋯⋯⋯⋯⋯⋯⋯
header3 = font2.render("About the Game", True, (WHITE))
text1 = font4.render("You are planning to build your own computer! For many months,", True, (WHITE))
text1_1 = font4.render("you have been saving up your money for this day. You decided", True, (WHITE))
text1_2 = font4.render("to buy the hardware components after your job since today was", True, (WHITE))
text1_3 = font4.render("payday(You gotta have that extra money ;)).", True, (WHITE))

header3_1 = font2.render("Word of Advice", True, (WHITE))
text2 = font4.render("<insert title> is a decision-based game, where your choices will", True, (WHITE))
text2_1 = font4.render("reflect your outcome result. Spend your money and choose your", True, (WHITE))
text2_2 = font4.render("choices wisely. You never know what consequences may occur...", True, (WHITE))

# ⋯⋯⋯⋯⋯⋯⋯⋯ Text (Scene 1) ⋯⋯⋯⋯⋯⋯⋯⋯
usertext = font3.render("User", True, (WHITE))
text3_1 = font4.render("Ahhh. Today is payday! I will finally have enough money to", True, (WHITE))
text3_2 = font4.render("build my computer. I better finish up quickly.", True, (WHITE))
text3_3 = font4.render("FINALLY! I better see the boss ot collect my paycheck.", True, (WHITE))


# Load next scene
scene = 1

#Loop until the user clicks the close button.
done = False
show_text = False
text_continue1 = False
 
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
                print("User pressed CONTINUE")
                q_click_position = pygame.key.get_pressed()
                if show_text == True:
                  show_text = False
                  text_continue1 = True
                # Disable the text display and enable continued text
                else:
                  show_text = True
                  text_continue1 = False
                # Enable text display and disable continued text
        elif event.type == pygame.MOUSEBUTTONDOWN:
          print("User pressed a mouse button.")
          mouse_click_position = pygame.mouse.get_pos()
    
    # # Starting page
    if scene == 1:
      screen.fill(BEIGE)

    # Other 
    elif scene == 2:
      screen.fill(DARK_BEIGE)
    elif scene == 3:
      screen.fill(DARK_BEIGE)
    else:
      screen.fill(BLUE_GREY)

    # Start Page 
    if scene == 1:
      screen.blit(test,(0,0))
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

    elif scene == 2:
      screen.blit(dog,(0,0))

      # Draw Button
      pygame.draw.rect(screen, RED, [returnbutton_x, returnbutton_y, returnbutton_width, returnbutton_height])

      # Check Button
      if (returnbutton_x <= mouse_click_position[0] and mouse_click_position[0] <= returnbutton_x + returnbutton_width) and (returnbutton_y <= mouse_click_position[1] and mouse_click_position[1] <= returnbutton_y + returnbutton_height):
          scene = 1
      
      # Text Box
      helpbox_x = 100
      helpbox_y = 90
      helpbox_width = 630
      helpbox_height = 450
     
      pygame.draw.rect(screen, BLACK,[helpbox_x, helpbox_y, helpbox_width, helpbox_height])

      # Text
      screen.blit(header3,(225,100))
      screen.blit(text1,(105,150))
      screen.blit(text1_1,(105,175))
      screen.blit(text1_2,(105,200))
      screen.blit(text1_3,(105,225))

      screen.blit(header3_1,(225,300))
      screen.blit(text2,(105,350))
      screen.blit(text2_1,(105,375))
      screen.blit(text2_2,(105,400))

    elif scene == 3:
      screen.blit(test2,(0,0)) 
      
     # Text Box
      textbox_x = 100
      textbox_y = 425
      textbox_width = 600
      textbox_height = 175
     
      pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])

      if show_text == True:
        screen.blit(usertext,(355,425))
        screen.blit(text3_1,(110,460))
        screen.blit(text3_2,(110,480))
      elif text_continue1 == True:
        screen.blit(usertext,(355,425))
        screen.blit(text3_3,(110,460))

      #if q_click_position

      
      


    # --- Game logic should go here
 
    # --- Drawing code should go here
     
    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.
    
     
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()