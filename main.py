""" 
A basic pygame template
"""
# ⋯⋯⋯⋯⋯⋯⋯⋯ 
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
MINT        = ( 244, 246, 240)

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
# ------------- Background -------------
job1 = pygame.image.load("scene-1.jpeg")
job1 = pygame.transform.smoothscale(job1, (800, 600))
job2 = pygame.image.load("scene-1.1.jpeg")
job2 = pygame.transform.smoothscale(job2, (800, 600))

#---------------------------------------
# --------------- Images ---------------
# Starting Page Images
test = pygame.image.load("test.jpg")
test = pygame.transform.smoothscale(test, (350, 250))

# Scene 1 Images
dog = pygame.image.load("dog.JPG")
dog = pygame.transform.smoothscale(dog, (500,300))
dog = pygame.transform.rotate(dog, -90)

test2 = pygame.image.load("other.png")
test2 = pygame.transform.smoothscale(test2, (350, 250))

money = pygame.image.load("money.png")
money = pygame.transform.smoothscale(money, (100,100))
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
dialogue1_1 = font4.render("\"Ahhh. Today is payday! I will finally have enough money to", True, (WHITE))
dialogue1_2 = font4.render("build my computer. I better finish up quickly.\"", True, (WHITE))
dialogue1_3 = font5.render("Few hours later", True, (WHITE))
dialogue1_4 = font4.render("\"FINALLY! I better see the boss ot collect my paycheck.\"", True, (WHITE))
dialogue2_1 = font4.render("\"Ahhh, there you are. I was wondering if you're willing to do", True, (WHITE))
dialogue2_2 = font4.render("a few more extra tasks before leaving.\"", True, (WHITE))

# Option 1 (Scene 1)
option1 = font4.render("\"Sure, I don’t have anything else to do.\"", True, (WHITE))
optdialogue1 = font4.render("\"Thank you so much! I’ll pay you more for overtime!\"", True, (WHITE))
optdialogue1_1 = font5.render("-- USER RECEIVES $450 --", True, (WHITE))

# Option 2 (Scene 1)
option2 = font4.render("\"Sorry, I need to do something right after this.\"", True, (WHITE))
optdialogue2 = font4.render("\"Oh, ok then, I’ll just give you your paycheck for this month.\"", True, (WHITE))
optdialogue2_1 = font5.render("-- USER RECEIVES $250 --", True, (WHITE))
banktext = font2.render("GO TO BANK", True, (WHITE))
#---------------------------------------
# Text Dialogue (Scene 2)
dialogue3_1 = font4.render("\"Alright. I'm going to withdrawal some money and see how", True, (WHITE))
dialogue3_2 = font4.render("much I have now.\"", True, (WHITE))
money_amt1 = font5.render("AMOUNT OF MONEY = $2450.00", True, (WHITE))
money_amt2 = font5.render("AMOUNT OF MONEY = $2250.00", True, (WHITE))
dialogue3_3 = font4.render("\"Now that's done, I'm going to go to the hardware store.\"", True, (WHITE))
#---------------------------------------
# Scene 3
dialogue4 = font5.render("USER GOES TO HARDWARE STORE", True, (WHITE))
dialogue5_1 = font4.render("\"Let's see... What should we start off with first? Hmmmm...", True, (WHITE))
dialogue5_2 = font4.render("I also cannot forget that all hardware components must be", True, (WHITE))
dialogue5_3 = font4.render("compatible with each other. \"", True, (WHITE))
dialogue5_4 = font4.render("\"I guess I'll start off with the CPU first.\"", True, (WHITE))

cpu_option1 = font4.render("AMD Ryzen 7 3700X", True, (WHITE))
cpu_option1_cost = font4.render("COST - $404.15", True, (WHITE))
cpu_option2 = font4.render("Intel Core i9-10900K", True, (WHITE))
cpu_option2_cost = font4.render("COST - $569.00", True, (WHITE))
#---------------------------------------
# GPU Choices (AMD Path)
dialogue5 = font4.render("\"Now let's choose the GPU.\"", True, (WHITE))
gpu_option1_1 = font4.render("NVIDIA GeForce RTX 3070 8GB", True, (WHITE))
gpu_option1_1cost = font4.render("COST = $679.99", True, (WHITE))
gpu_option1_2 = font4.render("Asus GeForce GTX 1660 SUPER 6 GB", True, (WHITE))
gpu_option1_2cost = font4.render("COST = $379.00", True, (WHITE))

# GPU Choices (Intel Path)
gpu_option2_1 = font4.render("MSI GeForce GTX 1660 Ti 6GB GAMING X", True, (WHITE))
gpu_option2_1cost = font4.render("COST = $439.99", True, (WHITE))
gpu_option2_2 = font4.render("MSI Radeon RX 580 8GB ARMOR OC", True, (WHITE))
gpu_option2_2cost = font4.render("COST = $539.00", True, (WHITE))
#--------------------------------------
# RAM Choices (AMD Path)
dialogue6 = font4.render("\"Now let's choose the RAM.\"", True, (WHITE))
ram_option1_1 = font4.render("Corsair Vengeance RGB Pro 32GB", True, (WHITE))
ram_option1_1cost = font4.render("COST = $229.00", True, (WHITE))
ram_option1_2 = font4.render("G.Skill Trident Z RGB 16GB", True, (WHITE))
ram_option1_2cost = font4.render("COST = $139.99", True, (WHITE))
#--------------------------------------
# Motherboard (AMD Path)
dialogue7 = font4.render("\"Now let's choose the Motherboard.\"", True, (WHITE))
motherboard_option1_1 = font4.render("Asus TUF GAMING X570-PLUS (WI-FI) ATX AM4 Motherboard", True, (WHITE))
motherboard_option1_1cost = font4.render("COST - $248.50", True, (WHITE))
motherboard_option1_2 = font4.render("MSI MAG B550 TOMAHAWK ATX AM4 Motherboard", True, (WHITE))
motherboard_option1_2cost = font4.render("COST - $199.99", True, (WHITE))
motherboard_option1_3 = font4.render("MSI B550-A PRO ATX AM4 Motherboard", True, (WHITE))
motherboard_option1_3cost = font4.render("COST - $184.99", True, (WHITE))

#--------------------------------------
# Hard-disk drive (AMD Path)
dialogue8 = font4.render("\"Now, should I get 1TB or 500GB for the SATA and M.2 SSD.\"", True, (WHITE))
ssd_option1_1 = font4.render("1TB TOTAL COST (FOR BOTH)= $270.34", True, (WHITE))
ssd_option1_2 = font4.render("500GB TOTAL COST (FOR BOTH)= $169.97", True, (WHITE))
#--------------------------------------
# Subtotal Cost For CPU, GPU, RAM, Motherboard and SSd
dialogue9 = font4.render("\"Alright. The current total cost is:\"", True, (WHITE))
#---------------------------------------
# Load next scene
scene = 0

# Show dialogue text
show_text = 1
show_textopt1 = 1
show_textopt2 = 1

#Loop until the user clicks the close button.
done = False
 
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
                show_textopt1 += 1
                show_textopt2 += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
          print("User pressed a mouse button.")
          mouse_click_position = pygame.mouse.get_pos()
    print("scene", scene)
    print("show_textopt1", show_textopt1)
    print("show_textopt2", show_textopt2)
    # Start Page 
    if scene == 0:
      # Fill background
      screen.fill(LIGHT_BEIGE)

      # Input images and/or text
      
      screen.blit(title1,(100,100))

      # Drawing Button
      pygame.draw.rect(screen, RED, [startbutton_x, startbutton_y, startbutton_width, startbutton_height])
      pygame.draw.rect(screen, GREEN, [helpbutton_x, helpbutton_y, helpbutton_width, helpbutton_height])
      
      # Checking Button
      if (startbutton_x <= mouse_click_position[0] and mouse_click_position[0] <= startbutton_x + startbutton_width) and (startbutton_y <= mouse_click_position[1] and mouse_click_position[1] <= startbutton_y + startbutton_height):
          scene = 2
      elif (helpbutton_x <= mouse_click_position[0] and mouse_click_position[0] <= helpbutton_x + helpbutton_width) and (helpbutton_y <= mouse_click_position[1] and mouse_click_position[1] <= helpbutton_y + helpbutton_height):
          scene = 1
      
      # Text
      screen.blit(header1,(500,325))
      screen.blit(header2,(160,325))
# ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
    # Help Page
    elif scene == 1:
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
          scene = 0
# ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
    # Scene 1
    elif scene == 2:
      # Fill background
      screen.blit(job1,(0,0))

      # Input images
      dog_rect = dog.get_rect()
      dog_rect.center = screen.get_rect().center
      screen.blit(dog,dog_rect)

      # Text Box
      pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
      
      # Show dialogue
      if show_text == 1:
        screen.blit(usertext, (usertext_x, 425))
        screen.blit(dialogue1_1,(110,460))
        screen.blit(dialogue1_2,(110,485)) 
      elif show_text == 2:
        screen.blit(dialogue1_3,(320,460))
      elif show_text == 3:
        screen.blit(usertext,(355,425))
        screen.blit(dialogue1_4,(110,460))
      elif show_text == 4:
        screen.blit(bosstext, [bosstext_x, 425]) 
        screen.blit(dialogue2_1,(110,460))
        screen.blit(dialogue2_2,(110,485))
      
      # Provide options
      else:
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(option1,(120,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(option2,(120,545)) 
      
      # Check Buttons
      if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
          scene = 3
      if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
          scene = 4
# ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
    # Option 1  
    elif scene == 3:
      # Fill background
      screen.blit(job2,(0,0))
      
      # Text Box
      pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])

      if show_textopt1 == 5:
        # Input images and/or text
        screen.blit(bosstext, [bosstext_x, 425])
        screen.blit(optdialogue1,(110,460))
        screen.blit(optdialogue1_1,(275,485))

      # BLIT MONEY IMG
        

      elif show_textopt1 == 6:
        # Draw Button (with Text)
        pygame.draw.rect(screen, SLATE_GREY, [nextscene1_x, nextscene1_y, nextscene1_width, nextscene1_height])
        screen.blit(banktext,(240,495))

        # Check Button
        if (nextscene1_x <= mouse_click_position[0] and mouse_click_position[0] <= nextscene1_x + nextscene1_width) and (nextscene1_y <= mouse_click_position[1] and mouse_click_position[1] <= nextscene1_y + nextscene1_height):
          scene = 5
          show_textopt1 += 1
# ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
    # Option 2
    elif scene == 4:
      # Fill background
      screen.fill(BLUE_GREY)
      
      # Text Box
      pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])

      if show_textopt2 == 5:
        # Input images and/or text
        screen.blit(bosstext, [bosstext_x, 425])
        screen.blit(optdialogue2,(110,460))
        screen.blit(optdialogue2_1,(275,485))

      elif show_textopt2 == 6:
        # Draw Button (with Text)
        pygame.draw.rect(screen, SLATE_GREY, [nextscene1_x, nextscene1_y, nextscene1_width, nextscene1_height])
        screen.blit(banktext,(240,495))

        # Check Button 
        if (nextscene1_x <= mouse_click_position[0] and mouse_click_position[0] <= nextscene1_x + nextscene1_width) and (nextscene1_y <= mouse_click_position[1] and mouse_click_position[1] <= nextscene1_y + nextscene1_height):
          scene = 6
          show_textopt2 += 1
#------------------------------------------------------     
    # Scene 2 (Option 1 Path)
    elif scene == 5:
      # Fill background
      screen.fill(MINT)

      # Text Box
      pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
      
      # Show dialogue
      if show_textopt1 == 7:
        screen.blit(usertext, (usertext_x, 425))
        screen.blit(dialogue3_1,(110,460))
        screen.blit(dialogue3_2,(110,480)) 
      if show_textopt1 == 8: 
        screen.blit(money_amt1,(110,460))
      elif show_textopt1 == 9:
        screen.blit(usertext, (usertext_x, 425))
        screen.blit(dialogue3_3,(110,460))
      elif show_textopt1 == 10:
        screen.blit(dialogue4,(240,460))
      elif show_textopt1 == 11:
        screen.blit(usertext, (usertext_x, 425))
        screen.blit(dialogue5_1,(110,460))
        screen.blit(dialogue5_2,(110,485))
        screen.blit(dialogue5_3,(110,510))
      elif show_textopt1 == 12:
        screen.blit(usertext, (usertext_x, 425))
        screen.blit(dialogue5_4,(110,460))
      
      # Provide options
      elif show_textopt1 == 13:
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(cpu_option1,(120,470))
        screen.blit(cpu_option1_cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(cpu_option2,(120,545)) 
        screen.blit(cpu_option2_cost,(525,545)) 
      
        # Check Buttons
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 7
            show_textopt1 += 1
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 8
            show_textopt2 += 1
# ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯    
    # Scene 2 (Option 2 Path)
    elif scene == 6:
      # Fill background
      screen.fill(BEIGE)

      # Text Box
      pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])

      # Input images
      
      
      # Show dialogue
      if show_textopt2 == 7:
        screen.blit(usertext, (usertext_x, 425))
        screen.blit(dialogue3_1,(110,460))
        screen.blit(dialogue3_2,(110,480)) 
      elif show_textopt2 == 8: 
        screen.blit(money_amt2,(110,460))
      elif show_textopt2 == 9:
        screen.blit(usertext, (usertext_x, 425))
        screen.blit(dialogue3_3,(110,460))
      elif show_textopt2 == 10:
        screen.blit(dialogue4,(110,460))
      elif show_textopt2 == 11:
        screen.blit(usertext, (usertext_x, 425))
        screen.blit(dialogue5_1,(110,460))
        screen.blit(dialogue5_2,(110,485))
        screen.blit(dialogue5_3,(110,510))
      elif show_textopt2 == 12:
        screen.blit(usertext, (usertext_x, 425))
        screen.blit(dialogue5_4,(110,460))
      
      
      # Provide options
      elif show_textopt2 == 13:
        # AMD CPU 
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(cpu_option1,(120,470))
        screen.blit(cpu_option1_cost,(525,470))
        # INTEL CPU
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(cpu_option2,(120,545)) 
        screen.blit(cpu_option2_cost,(525,545))
      
        # Check Buttons
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 9
            show_textopt1 += 1
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 10
            show_textopt2 += 1
#------------------------------------------------------    
    # AMD CPU: Picking GPU
    elif scene == 7:
      # Fill background
      screen.fill(WHITE)

      # Text Box
      pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])

      if show_textopt1 == 14:
        screen.blit(usertext, (usertext_x, 425))
        screen.blit(dialogue5,(110,460))

      elif show_textopt1 == 15:
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(gpu_option1_1,(120,470))
        screen.blit(gpu_option1_1cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(gpu_option1_2,(120,545)) 
        screen.blit(gpu_option1_2cost,(525,545))

    

# ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯      
    #else:
      #screen.fill(BEIGE)

    

        
      
      
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()