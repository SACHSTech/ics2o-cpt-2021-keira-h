"""
----------------------------------------------------------
Name:    main.py
Purpose: Produce a python program demonstrating your understanding of a variety of topics in the course.

Author:  Hosey.K

Created: date in 07/04/2021
----------------------------------------------------------
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
 
pygame.display.set_caption("Building My Computer")
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

button_pressed = False
mouse_click_position = [0,0]
#---------------------------------------
# --------------- Boxes ---------------
# Help Box 
helpbox_width = 630
helpbox_height = 450
helpbox_x = ((display_width/2) -(helpbox_width/2))
helpbox_y = 90

# Text Box
textbox_x = 100
textbox_y = 425
textbox_width = 600
textbox_height = 175
#---------------------------------------
# ------------- Background -------------
store = pygame.image.load("backgrounds/canada-computer.jpeg")
store = pygame.transform.smoothscale(store,  (800, 600))

job1 = pygame.image.load("backgrounds/scene-1.jpeg")
job1 = pygame.transform.smoothscale(job1, (800, 600))
job2 = pygame.image.load("backgrounds/scene-1.1.jpeg")
job2 = pygame.transform.smoothscale(job2, (800, 600))

bank = pygame.image.load("backgrounds/RBC-atm.jpeg")
bank = pygame.transform.smoothscale(bank,  (800, 600))

cpustore = pygame.image.load("backgrounds/canada-computer8.jpeg")
cpustore = pygame.transform.smoothscale(cpustore,  (800, 600))
gpustore = pygame.image.load("backgrounds/canada-computer9.jpeg")
gpustore = pygame.transform.smoothscale(gpustore,  (800, 600))
ramstore = pygame.image.load("backgrounds/canada-computer7.jpeg")
ramstore = pygame.transform.smoothscale(ramstore,  (800, 600))
mbstore = pygame.image.load("backgrounds/canada-computer4.jpeg")
mbstore = pygame.transform.smoothscale(mbstore,  (800, 600))
#---------------------------------------
# --------------- Images ---------------
# Characters
user1 = pygame.image.load("character/Work 2.png")
user1 = pygame.transform.smoothscale(user1, (400, 533))
user1_rect = user1.get_rect()
user1_rect.center = screen.get_rect().center

user2 = pygame.image.load("character/Work_(smile) 2.png")
user2 = pygame.transform.smoothscale(user2, (400, 533))
user2_rect = user2.get_rect()
user2_rect.center = screen.get_rect().center

user3 = pygame.image.load("character/casual 2.png")
user3 = pygame.transform.smoothscale(user3, (400, 533))
user3_rect = user3.get_rect()
user3_rect.center = screen.get_rect().center

user4 = pygame.image.load("character/casual_(sad) 2.png")
user4 = pygame.transform.smoothscale(user4, (400, 533))
user4_rect = user4.get_rect()
user4_rect.center = screen.get_rect().center

user5 = pygame.image.load("character/casual_(smile).png")
user5 = pygame.transform.smoothscale(user5, (400, 533))
user5_rect = user5.get_rect()
user5_rect.center = screen.get_rect().center

boss = pygame.image.load("character/boss 2.png")
boss = pygame.transform.smoothscale(boss, (400, 533))
boss_rect = boss.get_rect()
boss_rect.center = screen.get_rect().center
#---------------------------------------
# ----------- Fonts and Text -----------
# Fonts  
font1 = pygame.font.SysFont("freesans",70,bold=True)
font2 = pygame.font.SysFont("freesans",50,bold=True)
font3 = pygame.font.SysFont("freesans",30,bold=True)
font4 = pygame.font.SysFont("freesans",20,bold=True)
font5 = pygame.font.SysFont("freesans",20,bold=True,italic=True)
#---------------------------------------
# Text (Starting Page)
title1 = font1.render("Building My Computer", True, (BLACK))
title1_rect = title1.get_rect()
title1_rect.center = screen.get_rect().center
title1_x = title1.get_rect(center=(display_width/2,150))
header1 = font2.render("START", True, (BLACK))
header2 = font2.render("HELP", True, (BLACK))
#---------------------------------------
# Text (Help Page) 
header3 = font2.render("About the Game", True, (WHITE))
header3_rect = header3.get_rect()
header3_rect.center = screen.get_rect().center
header3_x = header3.get_rect(center=(display_width/2,120))

text1 = font4.render("You are planning to build your own computer! For many months,", True, (WHITE))
text1_1 = font4.render("you have been saving up your money for this day. You decided", True, (WHITE))
text1_2 = font4.render("to buy the hardware components after your job since today was", True, (WHITE))
text1_3 = font4.render("payday ( You gotta have that extra money ;) ).", True, (WHITE))
text1_4 = font4.render("Use \"Q\" to continue through the dialogue.", True, (WHITE))
text1_4_rect = text1_4.get_rect()
text1_4_rect.center = screen.get_rect().center
text1_4_x = text1_4.get_rect(center=(display_width/2,290))
returntext = font3.render("Return Home", True, (WHITE)) 

header3_1 = font2.render("Keep in Mind...", True, (WHITE))
header3_1_rect = header3_1.get_rect()
header3_1_rect.center = screen.get_rect().center
header3_1_x = header3_1.get_rect(center=(display_width/2,350))
text2 = font4.render("In Buying My Computer, your choices will reflect your outcome", True, (WHITE))
text2_1 = font4.render("result. Spend your money and choose your choices wisely.", True, (WHITE))
text2_2 = font4.render("You never know, you can go over your budget... (*._.)", True, (WHITE))
text2_3 = font4.render("You will NOT know how much money you have left until", True, (WHITE))
text2_3_rect = text2_3.get_rect()
text2_3_rect.center = screen.get_rect().center
text2_3_x = text2_3.get_rect(center=(display_width/2,475))
text2_4 = font4.render("the VERY END (cash register). (∙ ε ∙ ` *)…", True, (WHITE))
text2_4_rect = text2_4.get_rect()
text2_4_rect.center = screen.get_rect().center
text2_4_x = text2_4.get_rect(center=(display_width/2,500))
#---------------------------------------
# Text Titles
usertext = font3.render("User", True, (WHITE))
usertext_rect = usertext.get_rect()
usertext_rect.center = screen.get_rect().center
usertext_x = usertext.get_rect(center=(display_width/2,440)) 

bosstext = font3.render("Boss", True, (WHITE))
bosstext_rect = bosstext.get_rect()
bosstext_rect.center = screen.get_rect().center
bosstext_x = bosstext.get_rect(center=(display_width/2,440))

# Reminder
remind_text = font5.render("Please click the screen before proceeding to avoid errors.", True, (WHITE))
remind_text_centre = remind_text.get_rect(center=(display_width/2,575))

# Game Over
gameover_text = font1.render("GAME OVER :(", True, (WHITE))
gameover_text_rect = gameover_text.get_rect()
gameover_text_rect.center = screen.get_rect().center
gameover_text_x = gameover_text.get_rect(center=(display_width/2,display_height/2)) 

# Win
win_text = font1.render("Congrats!", True, (WHITE))
win_text_rect = win_text.get_rect()
win_text_rect.center = screen.get_rect().center
win_text_x = win_text.get_rect(center=(display_width/2,display_height/2))
win_text1 = font4.render("You were able to make your computer without going over :)", True, (WHITE))
win_text1_rect = win_text1.get_rect()
win_text1_rect.center = screen.get_rect().center
win_text1_x = win_text1.get_rect(center=(display_width/2,350))

#---------------------------------------
# Text Dialogue (Scene 1)
dialogue1_1 = font4.render("\"Ahhh. Today is payday! I will finally have enough money to", True, (WHITE))
dialogue1_2 = font4.render("build my computer. I better finish up quickly.\"", True, (WHITE))
dialogue1_3 = font5.render("Few hours later", True, (WHITE))
dialogue1_3_centre = dialogue1_3.get_rect(center=(display_width/2,470))
dialogue1_4 = font4.render("\"FINALLY! I better see the boss to collect my paycheck.\"", True, (WHITE))
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
money_amt1 = font5.render("AMOUNT OF MONEY = $2650.00", True, (WHITE))
money_amt1_centre = money_amt1.get_rect(center=(display_width/2,465))
money_amt2 = font5.render("AMOUNT OF MONEY = $2000.00", True, (WHITE))
money_amt2_centre = money_amt2.get_rect(center=(display_width/2,465))
dialogue3_3 = font4.render("\"Now that's done, I'm going to go to the hardware store.\"", True, (WHITE))
dialogue3_4 = font4.render("\"Oh no! I won't have enough to buy the hardwares since the", True, (WHITE))
dialogue3_5 = font4.render("components I planned out already are $1140.76. Hardwares", True, (WHITE))
dialogue3_6 = font4.render("are expensive :(. I guess I will have to wait for next month...\"", True, (WHITE))
#---------------------------------------
# Scene 3
dialogue4 = font5.render("USER GOES TO HARDWARE STORE", True, (WHITE))
dialogue4centre = dialogue4.get_rect(center=(display_width/2,470))
dialogue4_1 = font4.render("\"Let's see... I already planned out my SSDs, PSU, Case,", True, (WHITE))
dialogue4_2 = font4.render("Keyboard, Mouse, Monitor and Operating System. The cost", True, (WHITE))
dialogue4_3 = font4.render("for those components were $1140.76. Now I just need the", True, (WHITE))
dialogue4_4 = font4.render("CPU, GPU, RAM, and Motherboard.\"", True, (WHITE))
dialogue4_5 = font4.render("\"I guess I'll start off with the CPU first.\"", True, (WHITE))

cpu_option1 = font4.render("AMD Ryzen 7 3700X", True, (WHITE))
cpu_option1_cost = font4.render("COST - $399.99", True, (WHITE))
cpu_option2 = font4.render("Intel Core i9-10900K", True, (WHITE))
cpu_option2_cost = font4.render("COST - $569.00", True, (WHITE))
#---------------------------------------
# GPU Choices (AMD Path)
dialogue5 = font4.render("\"Now let's choose the GPU.\"", True, (WHITE))
gpu_option1_1 = font4.render("NVIDIA GeForce RTX 3070 8GB", True, (WHITE))
gpu_option1_1cost = font4.render("COST = $679.99", True, (WHITE))
gpu_option1_2 = font4.render("Sapphire Radeon RX 5700 XT 8GB", True, (WHITE))
gpu_option1_2cost = font4.render("COST - $573.62", True, (WHITE))

# GPU Choices (Intel Path)
dialogue5_1 = font4.render("\"I need to get a CPU cooler. I'm going to get the one that", True, (WHITE))
dialogue5_2 = font4.render("costs $39.99. Now for the cost of the PSU, Case, Keyboard,", True, (WHITE))
dialogue5_3 = font4.render("Mouse, Monitor, Operating System, Hard-Drive Disk,", True, (WHITE))
dialogue5_4 = font4.render("and CPU Cooler is $1180.75. Now let's choose the GPU.\"", True, (WHITE))
gpu_option2_1 = font4.render("MSI GeForce GTX 1660 SUPER 6GB GAMING X", True, (WHITE))
gpu_option2_1cost = font4.render("COST - $420.00", True, (WHITE))
gpu_option2_2 = font4.render("EVGA GeForce GTX 1650 SUPER 4GB", True, (WHITE))
gpu_option2_2cost = font4.render("COST - $275.99", True, (WHITE))
#--------------------------------------
# RAM Choices (AMD and Intel Path)
dialogue6 = font4.render("\"Now let's choose the RAM.\"", True, (WHITE))
ram_option1_1 = font4.render("Corsair Vengeance RGB Pro 32GB", True, (WHITE))
ram_option1_1cost = font4.render("COST = $229.00", True, (WHITE))
ram_option1_2 = font4.render("G.Skill Trident Z RGB 16GB", True, (WHITE))
ram_option1_2cost = font4.render("COST = $139.99", True, (WHITE))
#--------------------------------------
# Motherboard (AMD Path)
dialogue7 = font4.render("\"Now let's choose the Motherboard.\"", True, (WHITE))
motherboard_option1_1 = font4.render("Asus TUF GAMING X570-PLUS (WIFI)", True, (WHITE))
motherboard_option1_1cost = font4.render("COST - $248.50", True, (WHITE))
motherboard_option1_2 = font4.render("MSI B550-A PRO", True, (WHITE))
motherboard_option1_2cost = font4.render("COST - $184.99", True, (WHITE))
motherboard_option1_3 = font4.render("MSI MAG B550 TOMAHAWK", True, (WHITE))
motherboard_option1_3cost = font4.render("COST - $199.99", True, (WHITE))
motherboard_option1_4 = font4.render("Gigabyte X570 AORUS ULTRA", True, (WHITE))
motherboard_option1_4cost = font4.render("COST - $400.50", True, (WHITE))
motherboard_option1_5 = font4.render("Asus ROG Crosshair VIII Hero (WIFI)", True, (WHITE))
motherboard_option1_5cost = font4.render("COST - $499.00", True, (WHITE))

# Motherboard (Intel Path)
motherboard_option2_1 = font4.render("MSI MPG Z490 GAMING PLUS", True, (WHITE))
motherboard_option2_1cost = font4.render("COST - $225.75", True, (WHITE))
motherboard_option2_2 = font4.render("MSI MEG Z490 ACE", True, (WHITE))
motherboard_option2_2cost = font4.render("COST - $508.50", True, (WHITE))
motherboard_option2_3 = font4.render("Gigabyte Z490 AORUS MASTER", True, (WHITE))
motherboard_option2_3cost = font4.render("COST - $499.00", True, (WHITE))
motherboard_option2_4 = font4.render("Asus ROG STRIX Z490-E GAMING", True, (WHITE))
motherboard_option2_4cost = font4.render("COST - $379.99", True, (WHITE))
motherboard_option2_5 = font4.render("MSI MEG Z490 ACE", True, (WHITE))
motherboard_option2_5cost = font4.render("COST - $508.50", True, (WHITE))
#--------------------------------------
# Total Cost For CPU, GPU, RAM, and Motherboard 
dialogue8 = font4.render("\"Alright. The total cost + $1140.76 is:", True, (WHITE))
dialogue8_1 = font4.render("\"Alright. The total cost + $1180.75 is:", True, (WHITE))
route1 = font4.render("$2698.24", True,(WHITE)) # OVER BUDGET
route2 = font4.render("$2634.73", True,(WHITE))
route3 = font4.render("$2761.23", True,(WHITE)) # OVER BUDGET
route4 = font4.render("$2560.72", True,(WHITE))
route5 = font4.render("$2743.87", True,(WHITE)) # OVER BUDGET
route6 = font4.render("$2591.87", True,(WHITE))
route7 = font4.render("$2439.35", True,(WHITE))
route8 = font4.render("$2753.36", True,(WHITE)) # OVER BUDGET
route9 = font4.render("$2625.49", True,(WHITE))
route10 = font4.render("$2908.24", True,(WHITE)) # OVER BUDGET
route11 = font4.render("$2809.73", True,(WHITE)) # OVER BUDGET
route12 = font4.render("$2536.48", True,(WHITE))
route13 = font4.render("$2635.72", True,(WHITE))
route14 = font4.render("$2764.23", True,(WHITE)) # OVER BUDGET
route15 = font4.render("$2546.71", True,(WHITE))
route16 = font4.render("$2665.72", True,(WHITE)) # OVER BUDGET

dialogue8_2 = font4.render("Phew, thank god I did not go over my budget\"", True, (WHITE))
dialogue8_3 = font4.render("Damn... I went over my budget... Welp... I guess... I guess I'll", True, (WHITE))
dialogue8_4 = font4.render("have to wait next month...\"", True, (WHITE))
#---------------------------------------
# Load next scene
scene = 0

# Show dialogue text
show_text = 1
show_textopt1 = 1
show_textopt2 = 1

#Loop until the user clicks the close button.
done = False
gameover = False
 
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
                show_text += 1
                show_textopt1 += 1
                show_textopt2 += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
          print("User pressed a mouse button.")
          mouse_click_position = pygame.mouse.get_pos()
# ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
    # Start Page 
    if scene == 0:
      # Fill background
      screen.fill(LIGHT_BEIGE)

      # Input text
      screen.blit(title1,title1_x)

      # Drawing Button
      pygame.draw.rect(screen, DARK_GREEN, [startbutton_x, startbutton_y, startbutton_width, startbutton_height])
      screen.blit(header1,(497,325))
      pygame.draw.rect(screen, SLATE_GREY, [helpbutton_x, helpbutton_y, helpbutton_width, helpbutton_height])
      screen.blit(header2,(160,325))
      
      # Checking Button
      if (startbutton_x <= mouse_click_position[0] and mouse_click_position[0] <= startbutton_x + startbutton_width) and (startbutton_y <= mouse_click_position[1] and mouse_click_position[1] <= startbutton_y + startbutton_height):
          scene = 2
      elif (helpbutton_x <= mouse_click_position[0] and mouse_click_position[0] <= helpbutton_x + helpbutton_width) and (helpbutton_y <= mouse_click_position[1] and mouse_click_position[1] <= helpbutton_y + helpbutton_height):
          scene = 1
      
# ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
    # Help Page
    elif scene == 1:
      # Fill background
      screen.fill(DARK_BEIGE)

      # Text Box
      pygame.draw.rect(screen, BLACK,[helpbox_x, helpbox_y, helpbox_width, helpbox_height])

      # Input images and/or text
      screen.blit(header3, header3_x)
      screen.blit(text1,(90,150))
      screen.blit(text1_1,(90,175))
      screen.blit(text1_2,(90,200))
      screen.blit(text1_3,(90,225))
      screen.blit(text1_4,text1_4_x)

      screen.blit(header3_1,header3_1_x)
      screen.blit(text2,(90,375))
      screen.blit(text2_1,(90,400))
      screen.blit(text2_2,(90,425))
      screen.blit(text2_3,text2_3_x)
      screen.blit(text2_4,text2_4_x)

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
      
      # Show dialogue
      if show_text == 1:
        # Input images
        screen.blit(user1,user1_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue1_1,(110,460))
        screen.blit(dialogue1_2,(120,485)) 
      elif show_text == 2:
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(dialogue1_3,dialogue1_3_centre)
      elif show_text == 3:
        # Input images
        screen.blit(user2,user2_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext,(355,425))
        screen.blit(dialogue1_4,(110,460))
      elif show_text == 4:
        # Input images
        screen.blit(boss,boss_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(bosstext, bosstext_x)
        screen.blit(dialogue2_1,(110,460))
        screen.blit(dialogue2_2,(120,485))
      
      # Provide options
      else:
        # Input images
        screen.blit(boss,boss_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(option1,(120,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(option2,(120,545)) 
      
      # Check Buttons
      if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
          scene = 3
          show_textopt1 = 5
      if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
          scene = 4
          show_textopt2 = 5
# ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
    # Option 1  
    elif scene == 3:
      # Fill background
      screen.blit(job2,(0,0))

      if show_textopt1 == 5:
        # Input images
        screen.blit(boss,boss_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(bosstext, bosstext_x)
        screen.blit(optdialogue1,(110,460))
        screen.blit(optdialogue1_1,(275,485))
        screen.blit(remind_text,remind_text_centre)

      elif show_textopt1 >= 6:
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
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
      screen.blit(job2,(0,0))

      if show_textopt2 == 5:
        # Input images
        screen.blit(boss,boss_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(bosstext, bosstext_x)
        screen.blit(optdialogue2,(110,460))
        screen.blit(optdialogue2_1,(275,485))
        screen.blit(remind_text,remind_text_centre)

      elif show_textopt2 >= 6:
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button (with Text)
        pygame.draw.rect(screen, SLATE_GREY, [nextscene1_x, nextscene1_y, nextscene1_width, nextscene1_height])
        screen.blit(banktext,(240,495))

        # Check Button 
        if (nextscene1_x <= mouse_click_position[0] and mouse_click_position[0] <= nextscene1_x + nextscene1_width) and (nextscene1_y <= mouse_click_position[1] and mouse_click_position[1] <= nextscene1_y + nextscene1_height):
          scene = 6
          show_textopt2 = 7
#------------------------------------------------------     
    # Scene 2 (Option 1 Path)
    elif scene == 5:
      # Fill background
      screen.blit(bank,(0,0))
      
      # Show dialogue
      if show_textopt1 == 7:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue3_1,(110,460))
        screen.blit(dialogue3_2,(120,480)) 
      if show_textopt1 == 8:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(money_amt1,money_amt1_centre)
      elif show_textopt1 == 9:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue3_3,(110,460))
      
      # User at Hardware Store 
      elif show_textopt1 == 10:
        screen.blit(cpustore,(0,0))
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(dialogue4,dialogue4centre)
      elif show_textopt1 == 11:
        # Background image
        screen.blit(cpustore,(0,0))
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue4_1,(110,460))
        screen.blit(dialogue4_2,(120,485))
        screen.blit(dialogue4_3,(120,510))
        screen.blit(dialogue4_4,(120,535))
      elif show_textopt1 == 12:
        # Background image
        screen.blit(cpustore,(0,0))
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue4_5,(110,460))
        screen.blit(remind_text,remind_text_centre)
      
      # Provide options
      elif show_textopt1 >= 13:
        # Background image
        screen.blit(cpustore,(0,0))
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(cpu_option1,(120,470))
        screen.blit(cpu_option1_cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(cpu_option2,(120,545)) 
        screen.blit(cpu_option2_cost,(525,545)) 
      
        # Check Buttons
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 7
            show_textopt1 = 14
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 22
            show_textopt2 = 14
# ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯    
    # Scene 2 (Option 2 Path)
    elif scene == 6:
      # Fill background
      screen.blit(bank,(0,0))

      # Show dialogue
      if show_textopt2 == 7:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue3_1,(110,460))
        screen.blit(dialogue3_2,(120,480)) 
      elif show_textopt2 == 8: 
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(money_amt2,money_amt2_centre)
      elif show_textopt2 == 9:
        # Input images
        screen.blit(user4,user4_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue3_4,(110,460))
        screen.blit(dialogue3_5,(120,485))
        screen.blit(dialogue3_6,(120,510))

      # Game Over
      if scene == 6 and show_textopt2 == 10:
        screen.fill(BLACK)
        screen.blit(gameover_text,gameover_text_x)
        gameover = True
      elif scene == 6 and show_textopt2 == 11:
        break
#------------------------------------------------------    
    # AMD CPU (Picking GPU)
    elif scene == 7:
      # Fill background
      screen.blit(gpustore,(0,0))

      if show_textopt1 == 14:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue5,(110,460))
        screen.blit(remind_text,remind_text_centre)

      elif show_textopt1 >= 15:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(gpu_option1_1,(120,470))
        screen.blit(gpu_option1_1cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(gpu_option1_2,(120,545)) 
        screen.blit(gpu_option1_2cost,(525,545))

        # Check Button
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 8
            show_textopt1 = 16
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 15
            show_textopt1 = 16
    
    # AMD CPU -- NVIDIA GPU (Picking RAM)
    elif scene == 8:
      # Fill background
      screen.blit(ramstore,(0,0))

      if show_textopt1 == 16:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue6,(110,460))
        screen.blit(remind_text,remind_text_centre)
      elif show_textopt1 >= 17:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(ram_option1_1,(120,470))
        screen.blit(ram_option1_1cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(ram_option1_2,(120,545)) 
        screen.blit(ram_option1_2cost,(525,545))

        # Check Button
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 9
            show_textopt1 = 18
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 16
            show_textopt1 = 18
    
    # AMD CPU -- NVIDIA GPU -- Corsair RAM (Picking Motherboard)
    elif scene == 9:
      # Fill background
      screen.blit(mbstore,(0,0))

      if show_textopt1 == 18:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue7,(110,460))
        screen.blit(remind_text,remind_text_centre)
      
      elif show_textopt1 >= 19:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(motherboard_option1_1,(120,470))
        screen.blit(motherboard_option1_1cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(motherboard_option1_2,(120,545))
        screen.blit(motherboard_option1_2cost,(525,545))

        # Check Button
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 10
            show_textopt1 = 20
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 11
            show_textopt1 = 20

    # AMD CPU -- NVIDIA GPU -- Corsair RAM -- Asus TUF MOTHERBOARD (FINAL) 
    elif scene == 10:
      # Fill background
      screen.blit(store,(0,0))

      if show_textopt1 == 20:
        # Input images
        screen.blit(user4,user4_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8,(110,460))
        screen.blit(route1,(475,460))
        screen.blit(dialogue8_3,(120,485))
        screen.blit(dialogue8_4,(120,510))
      
      if scene == 10 and show_textopt1 == 21:
        screen.fill(BLACK)
        screen.blit(gameover_text,gameover_text_x)
        gameover = True
      elif scene == 10 and show_textopt1 == 22:
        break


    # AMD CPU -- NVIDIA GPU -- Corsair RAM -- MSI B550-A MOTHERBOARD (FINAL)
    elif scene == 11:
      # Fill background
      screen.blit(store,(0,0))

      if show_textopt1 == 20:
        # Input images
        screen.blit(user5,user5_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8,(110,460))
        screen.blit(route2,(475,460))
        screen.blit(dialogue8_2,(120,485))
      
      # Win
      if scene == 11 and show_textopt1 == 21:
        screen.fill(BLUE_GREY)
        screen.blit(win_text,win_text_x)
        screen.blit(win_text1,win_text1_x)
      elif scene == 11 and show_textopt1 == 22:
        break


    # AMD CPU -- NVIDIA GPU -- G.Skill RAM (PICKING MOTHERBOARD)
    elif scene == 12:
      # Fill background
      screen.blit(mbstore,(0,0))

      if show_textopt1 == 18:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue7,(110,460))
        screen.blit(remind_text,remind_text_centre)

      elif show_textopt1 >= 19:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(motherboard_option1_4,(120,470))
        screen.blit(motherboard_option1_4cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(motherboard_option1_2,(120,545))
        screen.blit(motherboard_option1_2cost,(525,545))
        
        # Check Button
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 13
            show_textopt1 = 20
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 14
            show_textopt1 = 20
    
    # AMD CPU -- NVIDIA GPU -- G.Skill RAM -- GIGABYTE X570 MOTHERBOARD (FINAL) 
    elif scene == 13:
      # Fill background
      screen.blit(store,(0,0))

      if show_textopt1 == 20:
        # Input images
        screen.blit(user4,user4_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8,(110,460))
        screen.blit(route3,(475,460))
        screen.blit(dialogue8_3,(120,485))
        screen.blit(dialogue8_4,(120,510))
      
      # Game Over
      if scene == 13 and show_textopt1 == 21:
        screen.fill(BLACK)
        screen.blit(gameover_text,gameover_text_x)
        gameover = True
      elif scene == 13 and show_textopt1 == 22:
        break

    # AMD CPU -- NVIDIA GPU -- G.Skill RAM -- MSI MAG MOTHERBOARD (FINAL) 
    elif scene == 14:
      # Fill background
      screen.blit(store,(0,0))

      if show_textopt1 == 20:
        # Input images
        screen.blit(user5,user5_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8,(110,460))
        screen.blit(route4,(475,460))
        screen.blit(dialogue8_2,(120,485))
        
      # Win
      if scene == 14 and  show_textopt1 == 21:
        screen.fill(BLUE_GREY)
        screen.blit(win_text,win_text_x)
        screen.blit(win_text1,win_text1_x)
      elif scene == 14 and show_textopt1 == 22:
        break

# ⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
    # AMD CPU -- SAPPHIRE GPU (PICKING RAM)
    elif scene == 15:
      # Fill background
      screen.blit(ramstore,(0,0))

      if show_textopt1 == 16:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue6,(110,460))
        screen.blit(remind_text,remind_text_centre)
      elif show_textopt1 >= 17:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(ram_option1_1,(120,470))
        screen.blit(ram_option1_1cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(ram_option1_2,(120,545)) 
        screen.blit(ram_option1_2cost,(525,545))
        
        # Check Button
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 16
            show_textopt1 = 18
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 19
            show_textopt1 = 18

    # AMD CPU -- SAPPHIRE GPU -- Corsair RAM (Picking Motherboard)
    elif scene == 16:
      # Fill background
      screen.blit(mbstore,(0,0))

      if show_textopt1 == 18:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue7,(110,460))
        screen.blit(remind_text,remind_text_centre)

      elif show_textopt1 >= 19:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(motherboard_option1_3,(120,470))
        screen.blit(motherboard_option1_3cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(motherboard_option1_4,(120,545))
        screen.blit(motherboard_option1_4cost,(525,545))
        
        # Check Button
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 17
            show_textopt1 = 20
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 18
            show_textopt1 = 20
    
    # AMD CPU -- SAPPHIRE GPU -- Corsair RAM -- MSI MAG Motherboard (FINAL)
    elif scene == 17:
      # Fill background
      screen.blit(store,(0,0))

      if show_textopt1 == 20:
        # Input images
        screen.blit(user4,user4_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8,(110,460))
        screen.blit(route5,(475,460))
        screen.blit(dialogue8_3,(120,485))
        screen.blit(dialogue8_4,(120,510))
      
      # Game Over 
      if scene == 17 and show_textopt1 == 21:
        screen.fill(BLACK)
        screen.blit(gameover_text,gameover_text_x)
        gameover = True
      elif scene == 17 and show_textopt1 == 22:
        break
    
    # AMD CPU -- SAPPHIRE GPU -- Corsair RAM -- GIGABYTE X570 MOTHERBOARD (FINAL)
    elif scene == 18:
      # Fill background
      screen.blit(store,(0,0))

      if show_textopt1 == 20:
        # Input images
        screen.blit(user5,user5_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8,(110,460))
        screen.blit(route6,(475,460))
        screen.blit(dialogue8_2,(120,485))
      
      # Win
      if scene == 18 and  show_textopt1 == 21:
        screen.fill(BLUE_GREY)
        screen.blit(win_text,win_text_x)
        screen.blit(win_text1,win_text1_x)
      elif scene == 18 and show_textopt1 == 22:
        break

    # AMD CPU -- SAPPHIRE GPU -- G.Skill Trident RAM (Picking Motherboard)
    elif scene == 19:
      # Fill background
      screen.blit(mbstore,(0,0))

      if show_textopt1 == 18:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue7,(110,460))
        screen.blit(remind_text,remind_text_centre)

      elif show_textopt1 >= 19:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button 
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(motherboard_option1_2,(120,470))
        screen.blit(motherboard_option1_2cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(motherboard_option1_5,(120,545))
        screen.blit(motherboard_option1_5cost,(525,545))
        
        # Check Button
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 20
            show_textopt1 = 20
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 21
            show_textopt1 = 20
    
    # AMD CPU -- SAPPHIRE GPU -- G.Skill Trident RAM -- MSI B550-A MOTHERBOARD (FINAL)
    elif scene == 20:
      # Fill background
      screen.blit(store,(0,0))

      if show_textopt1 == 20:
        # Input images
        screen.blit(user5,user5_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8,(110,460))
        screen.blit(route7,(475,460))
        screen.blit(dialogue8_2,(120,485))
      
      # Win
      if scene == 20 and  show_textopt1 == 21:
        screen.fill(BLUE_GREY)
        screen.blit(win_text,win_text_x)
        screen.blit(win_text1,win_text1_x)
      elif scene == 20 and show_textopt1 == 22:
        break
      
    # AMD CPU -- SAPPHIRE GPU -- G.Skill Trident RAM -- ASUS ROG CROSSHAIR MOTHEROARD (FINAL) 
    elif scene == 21:
      # Fill background
      screen.blit(store,(0,0))

      if show_textopt1 == 20:
        # Input images
        screen.blit(user4,user4_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8,(110,460))
        screen.blit(route8,(475,460))
        screen.blit(dialogue8_3,(120,485))
        screen.blit(dialogue8_4,(120,510))
      
      # Game Over
      if scene == 21 and show_textopt1 == 21:
        screen.fill(BLACK)
        screen.blit(gameover_text,gameover_text_x)
        gameover = True
      elif scene == 21 and show_textopt1 == 22:
        break

#------------------------------------------------------ 
    # INTEL CPU (Picking GPU)
    elif scene == 22:
      # Fill background
      screen.blit(gpustore,(0,0))

      if show_textopt2 == 14:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue5_1,(110,460))
        screen.blit(dialogue5_2,(120,485))
        screen.blit(dialogue5_3,(120,510))
        screen.blit(dialogue5_4,(120,535))
        screen.blit(remind_text,remind_text_centre)
      elif show_textopt2 >= 15:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(gpu_option2_1,(120,470))
        screen.blit(gpu_option2_1cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(gpu_option2_2,(120,545)) 
        screen.blit(gpu_option2_2cost,(525,545))

        # Check Button
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 23
            show_textopt2 = 16
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 30
            show_textopt2 = 16 
    
    # INTEL CPU -- MSI GPU (Picking RAM)
    elif scene == 23:
      # Fill background
      screen.blit(ramstore,(0,0))

      if show_textopt2 == 16:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue6,(110,460))
        screen.blit(remind_text,remind_text_centre)
      elif show_textopt2 >= 17:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(ram_option1_1,(120,470))
        screen.blit(ram_option1_1cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(ram_option1_2,(120,545)) 
        screen.blit(ram_option1_2cost,(525,545))

        # Check Button
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 24
            show_textopt2 = 18
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 27
            show_textopt2 = 18
    
    # INTEL CPU -- MSI GPU -- Corsair RAM (Picking Motherboard)
    elif scene == 24:
      # Fill background
      screen.blit(mbstore,(0,0))

      if show_textopt2 == 18:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue7,(110,460))
        screen.blit(remind_text,remind_text_centre) 
      elif show_textopt2 >= 19:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(motherboard_option2_1,(120,470))
        screen.blit(motherboard_option2_1cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(motherboard_option2_2,(120,545))
        screen.blit(motherboard_option2_2cost,(525,545))

        # Check Button
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 25
            show_textopt2 = 20
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 26
            show_textopt2 = 20

    # INTEL CPU -- MSI GPU -- Corsair RAM -- MSI MPG PLUS MOTHERBOARD (FINAL) 
    elif scene == 25:
      # Fill background
      screen.blit(store,(0,0))

      if show_textopt2 == 20:
        # Input images
        screen.blit(user5,user5_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8_1,(110,460))
        screen.blit(route9,(475,460))
        screen.blit(dialogue8_2,(120,485))
      
      # Win
      if scene == 25 and  show_textopt2 == 21:
        screen.fill(BLUE_GREY)
        screen.blit(win_text,win_text_x)
        screen.blit(win_text1,win_text1_x)
      elif scene == 25 and show_textopt2 == 22:
        break

    # INTEL CPU -- MSI GPU -- Corsair RAM -- MSI MEG MOTHERBOARD (FINAL)
    elif scene == 26:
      # Fill background
      screen.blit(store,(0,0))
      if show_textopt2 == 20:
        # Input images
        screen.blit(user4,user4_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8_1,(110,460))
        screen.blit(route10,(475,460))
        screen.blit(dialogue8_3,(120,485))
        screen.blit(dialogue8_4,(120,510))
      
      # Game Over
      if scene == 26 and show_textopt2 == 21:
        screen.fill(BLACK)
        screen.blit(gameover_text,gameover_text_x)
        gameover = True
      elif scene == 26 and show_textopt2 == 22:
        break
    
    # INTEL CPU -- MSI GPU -- G.Skill RAM (Picking Motherboard)
    elif scene == 27:
      # Fill background
      screen.blit(mbstore,(0,0))

      if show_textopt2 == 18:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue7,(110,460))
        screen.blit(remind_text,remind_text_centre)
      
      elif show_textopt2 >= 19:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(motherboard_option2_3,(120,470))
        screen.blit(motherboard_option2_3cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(motherboard_option2_1,(120,545))
        screen.blit(motherboard_option2_1cost,(525,545))

        # Check Button
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 28
            show_textopt2 = 20
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 29
            show_textopt2 = 20

    # INTEL CPU -- MSI GPU -- Corsair RAM -- GIGABYTE Z490 MOTHERBOARD (FINAL) 
    elif scene == 28:
      # Fill background
      screen.blit(store,(0,0))

      if show_textopt2 == 20:
        # Input images
        screen.blit(user4,user4_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8_1,(110,460))
        screen.blit(route11,(475,460))
        screen.blit(dialogue8_3,(120,485))
        screen.blit(dialogue8_4,(120,510))
      
      # Game Over
      if scene == 28 and show_textopt2 == 21:
        screen.fill(BLACK)
        screen.blit(gameover_text,gameover_text_x)
        gameover = True
      elif scene == 28 and show_textopt2 == 22:
        break
      
    # INTEL CPU -- MSI GPU -- Corsair RAM -- MSI MPG MOTHERBOARD (FINAL)
    elif scene == 29:
      # Fill background
      screen.blit(store,(0,0))

      if show_textopt2 == 20:
        # Input images
        screen.blit(user5,user5_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8_1,(110,460))
        screen.blit(route12,(475,460))
        screen.blit(dialogue8_2,(120,485))
      
      # Win
      if scene == 29 and  show_textopt2 == 21:
        screen.fill(BLUE_GREY)
        screen.blit(win_text,win_text_x)
        screen.blit(win_text1,win_text1_x)
      elif scene == 29 and show_textopt2 == 22:
        break
    
    # INTEL CPU -- EVGA GPU (PICKING RAM)
    elif scene == 30:
      # Fill background
      screen.blit(ramstore,(0,0))

      if show_textopt2 == 16:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue6,(110,460))
        screen.blit(remind_text,remind_text_centre)
      elif show_textopt2 >= 17:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(ram_option1_1,(120,470))
        screen.blit(ram_option1_1cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(ram_option1_2,(120,545)) 
        screen.blit(ram_option1_2cost,(525,545))
        
        # Check Button
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 31
            show_textopt2 = 18
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 34
            show_textopt2 = 18
      
    # INTEL CPU -- EVGA GPU -- Corsair RAM (Picking Motherboard)
    elif scene == 31:
      # Fill background
      screen.blit(mbstore,(0,0))

      if show_textopt2 == 18:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue7,(110,460))
        screen.blit(remind_text,remind_text_centre)
      
      elif show_textopt2 >= 19:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(motherboard_option2_4,(120,470))
        screen.blit(motherboard_option2_4cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(motherboard_option2_2,(120,545))
        screen.blit(motherboard_option2_2cost,(525,545))

        # Check Button
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 32
            show_textopt2 = 20
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 33
            show_textopt2 = 20

    # INTEL CPU -- EVGA GPU -- Corsair RAM -- Asus ROG STRIX MOTHERBOARD (FINAL) 
    elif scene == 32:
      # Fill background
      screen.blit(store,(0,0))

      if show_textopt2 == 20:
        # Input images
        screen.blit(user5,user5_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8_1,(110,460))
        screen.blit(route13,(475,460))
        screen.blit(dialogue8_2,(120,485))
      
      # Win
      if scene == 32 and  show_textopt2 == 21:
        screen.fill(BLUE_GREY)
        screen.blit(win_text,win_text_x)
        screen.blit(win_text1,win_text1_x)
      elif scene == 32 and show_textopt2 == 22:
        break

    # INTEL CPU -- EVGA GPU -- Corsair RAM -- MSI MEG MOTHERBOARD (FINAL) 
    elif scene == 33:
      # Fill background
      screen.blit(store,(0,0))

      if show_textopt2 == 20:
        # Input images
        screen.blit(user4,user4_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8_1,(110,460))
        screen.blit(route14,(475,460))
        screen.blit(dialogue8_3,(120,485))
        screen.blit(dialogue8_4,(120,510))
      
      # Game Over
      if scene == 33 and show_textopt2 == 21:
        screen.fill(BLACK)
        screen.blit(gameover_text,gameover_text_x)
        gameover = True
      elif scene == 33 and show_textopt2 == 22:
        break
    
    # INTEL CPU -- EVGA GPU -- G.Skill RAM (Picking Motherboard)
    elif scene == 34:
      # Fill background
      screen.blit(mbstore,(0,0))

      if show_textopt2 == 18:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue7,(110,460))
        screen.blit(remind_text,remind_text_centre)
      
      elif show_textopt2 >= 19:
        # Input images
        screen.blit(user3,user3_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Draw Button
        pygame.draw.rect(screen, SLATE_GREY, [option1_x, option1_y, option1_width, option1_height])
        screen.blit(motherboard_option2_4,(120,470))
        screen.blit(motherboard_option2_4cost,(525,470))
        pygame.draw.rect(screen, DARK_GREEN, [option2_x, option2_y, option2_width, option2_height])
        screen.blit(motherboard_option2_2,(120,545))
        screen.blit(motherboard_option2_2cost,(525,545))

        # Check Button
        if (option1_x <= mouse_click_position[0] and mouse_click_position[0] <= option1_x + option1_width) and (option1_y <= mouse_click_position[1] and mouse_click_position[1] <= option1_y + option1_height):
            scene = 35
            show_textopt2 = 20
        if (option2_x <= mouse_click_position[0] and mouse_click_position[0] <= option2_x + option2_width) and (option2_y <= mouse_click_position[1] and mouse_click_position[1] <= option2_y + option2_height):
            scene = 36
            show_textopt2 = 20

    # INTEL CPU -- EVGA GPU -- G.Skill RAM -- Asus ROG STRIX MOTHERBOARD (FINAL) 
    elif scene == 35:
      # Fill background
      screen.blit(store,(0,0))

      if show_textopt2 == 20:
        # Input images
        screen.blit(user5,user5_rect)
        # Text box
        pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])
        # Dialogue
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8_1,(110,460))
        screen.blit(route15,(475,460))
        screen.blit(dialogue8_2,(120,485))
      
      # Win
      if scene == 35 and  show_textopt2 == 21:
        screen.fill(BLUE_GREY)
        screen.blit(win_text,win_text_x)
        screen.blit(win_text1,win_text1_x)
      elif scene == 35 and show_textopt2 == 22:
        break

    # INTEL CPU -- EVGA GPU -- G.Skill RAM -- GIGABYTE Z490 MOTHERBOARD (FINAL) 
    elif scene == 36:
      # Fill background
      screen.blit(store,(0,0))

      # Text Box
      pygame.draw.rect(screen, BLACK,[textbox_x, textbox_y, textbox_width, textbox_height])

      if show_textopt2 == 20:
        screen.blit(usertext, usertext_x)
        screen.blit(dialogue8_1,(110,460))
        screen.blit(route16,(475,460))
        screen.blit(dialogue8_3,(120,485))
        screen.blit(dialogue8_4,(120,510)) 
      
      # Game Over
      if scene == 36 and show_textopt2 == 21:
        screen.fill(BLACK)
        screen.blit(gameover_text,gameover_text_x)
        gameover = True
      elif scene == 36 and show_textopt2 == 22:
        break
        
      
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()