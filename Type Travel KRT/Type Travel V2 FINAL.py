# 'Type Travel' by Kris

# import the modules (REQUIRES TKINTER AND PIL TO BE INSTALLED)
from tkinter import *
from PIL import ImageTk,Image
import pygame
import random
import sys

# list of words
words = ['Resilience', 'Bravery', 'Benevolent', 'Eloquent', 'Elusive', 'Effervescence', 'Programming',
         'Algorithm', 'Amicable', 'Peaceful', 'Tranquility', 'Harmony', 'Authentic', 'Candor', 'Chivalrous',
         'Epic', 'Epitome', 'Ethereal', 'Elegant', 'Crimson', 'Chrome', 'Scarlet', 'Oath', 'Light', 'Galaxy','Void', 'Vermillion'
         ,'Vague', 'Unique', 'Tenacious', 'Serene', 'Rhetorical', 'Paradigm', 'Optimistically', 'Nostalgic', 'Narrative', 'Melancholy', 'Irony'
         , 'Integrity', 'Hyperbole', 'Fortitude', 'Empathy', 'Alliteration', 'Oxymoron', 'Contemplate', 'Introperspective', 'Luminescence', 'Magenta'
         , 'Magnanimous', 'Mindfulness', 'Nefarious', 'Quintessentially', 'Remarkable', 'Relentless', 'Exotic', 'Serendipitous', 'Splendiferous'
         , 'Stellar', 'Zealous', 'Intelligence', 'Astronomy', 'Constellations', 'Vigorous', 'Evocative', 'Precision', 'Accuracy', 'Ephemerality',
         'Immortality', 'Evanescent', 'Azure', 'Azalea', 'Antidisestablishmentarianism', 'James', 'Steve', 'Psychophysicotherapeutics', 'Discombobulate'
         , 'Legendary', 'Interstellar', 'Mountain', 'Hunter', 'Ascend']


# different font colours
colours = ['Red','Orange','Green', 'Blue', 'Purple', 'Turquoise', 'VioletRed3', 'MediumPurple3'
           , 'DeepSkyBlue3', 'SteelBlue2', 'light sea green', 'medium spring green', 'dodger blue'
           , 'DarkOrchid3', 'goldenrod3', 'SlateBlue1', 'chocolate3', 'gray9']


# score variables
score = 0
extra_time = 800
extra = 0
count = 0
correct = 0
missed = 0


# the game time left, initially set to 30 seconds
timeleft = 30 


# function that starts the game
def startGame(event):

        # deletes intro text
        g_canvas.delete(starting_1)
        g_canvas.delete(starting_2)
        g_canvas.delete(starting_3)
        g_canvas.delete(starting_4)
        g_canvas.pack()

        if timeleft == 30: 
                
                # start the countdown timer 
                countdown()
                
        # run the function to choose the next colour
        nextColour() 
    
# function to choose and display the next colour
def nextColour(): 

    # use the globally declared 'score' and 'play' variables above
    global score 
    global timeleft
    global count
    global correct
    global missed


    # if a game is currently in play 
    if timeleft > 0: 

            # make the text entry box active 
            e.focus_set() 

            # if the word entered matches the word being displayed
            if e.get().lower() == words[0].lower():
                score += 100
                correct += 1
                count += 1
                g_canvas.move(sprite11,sprite_vel,0)
                

                # after 8 words you receive extra time for every correct word
                if (int(score/extra_time)) > extra:
                    timeleft += 3
            elif e.get().lower() != words[0].lower():
                count += 1
                missed += 1
                

            # clear the text entry box
            e.delete(0, END) 
            
            random.shuffle(words) 
            random.shuffle(colours)
            
            # change the colour to type, by changing the text _and_ the colour to a random colour value 
            label.config(fg = str(colours[1]), text = str(words[0])) 
            
            # update the score 
            scoreLabel.config(text = "Score: " + str(score)) 


# Countdown timer function 
def countdown(): 
    global count
    global timeleft
    global music
    
    # if a game is in play 
    if timeleft > 0: 

        if score <= 4000:
            # decrement the timer
            timeleft -= 1
            
            # update the time left label
            timeLabel.config(text = "Time left: " + str(timeleft))
                                                            
            # run the function again after 1 second
            timeLabel.after(1000, countdown)

        else:
            # decrement the timer
            timeleft -= 2

            # update the time left label
            if timeleft >= 0:
                timeLabel.config(text="Time left: " + str(0))

            timeLabel.config(text="Time left: " + str(timeleft))

            # run the function again after 1 second
            timeLabel.after(1000, countdown)




       
    # game over screen
    elif timeleft <= 0:
        count -= 1
        if correct == 0:
            accuracy = 0

        else:
            accuracy = round((correct / count) * 100)




        game_over = g_canvas.create_text(m_x, 45, text='GAME OVER', fill='white', font=('fixedsys', 30))
        final_score = g_canvas.create_text(m_x, m_y+110, text='Score: ' + str(score), fill='white', font=('fixedsys', 20))
        words_correct = g_canvas.create_text(m_x, m_y+140, text='You typed %s/%s words successfully' % (str(correct), str(count)), fill='white', font=('fixedsys', 20))
        accuracy_percent = g_canvas.create_text(m_x, m_y+170, text='Word accuracy: %s%s' % (str(accuracy), str('%')) , fill='white', font=('fixedsys', 20))
        planet_score = g_canvas.create_text(m_x, m_y-600, text=score_reach(), fill='white', font=('fixedsys', 20))
        exit_game = g_canvas.create_text(m_x, m_y+210, text='Press "Esc" to close the game', fill='white', font=('fixedsys', 20))


        # music stops and game over sound is played
        pygame.mixer.quit()
        pygame.mixer.init()
        pygame.mixer.music.load('ducky_end.wav')
        pygame.mixer.music.play()

        
    
     
                                                     


# score feedback
def score_reach():                
    global score
    if int(score) >= 500 and int(score) < 1500:
        earth = g_canvas.create_text(m_x, m_y-60, text="""Congratulations!
        You've managed to travel to Earth!""", fill='white', font=('fixedsys', 20))

    elif int(score) >= 1500 and int(score) < 3000:
        mars = g_canvas.create_text(m_x, m_y-60, text="""Congratulations!
        You've managed to travel to Mars!""", fill='white', font=('fixedsys', 20))

    elif int(score) >= 3000 and int(score) < 4000:
        jupiter = g_canvas.create_text(m_x, m_y-60, text="""Congratulations!
        You've managed to travel to Jupiter!""", fill='white', font=('fixedsys', 20))

    elif int(score) >= 4000 and int(score) < 5000:
        saturn = g_canvas.create_text(m_x, m_y-60, text="""Congratulations!
        You've managed to travel to Saturn!""", fill='white', font=('fixedsys', 20))

    elif int(score) >= 5000 and int(score) < 6000:
        uranus = g_canvas.create_text(m_x, m_y-60, text="""Congratulations!
        You've managed to travel to Uranus!""", fill='white', font=('fixedsys', 20))

    elif int(score) >= 6000 and int(score) >= 6700:
        neptune = g_canvas.create_text(m_x, m_y-60, text="""Congratulations!
        You've managed to travel to Neptune!""", fill='white', font=('fixedsys', 20))

    elif int(score) >= 7000:
        speedy = g_canvas.create_text(m_x, m_y-60, text="""Congratulations!
        You have managed to travel far and beyond the edges of the solar system!""", fill='white', font=('fixedsys', 20))
        
    else:
        no_planets = g_canvas.create_text(m_x, m_y-60, text="""Unfortunately you couldn't reach any of the planets""",
                                          fill='white', font=('fixedsys', 20))

                                     
# terminates the program and 
def startMusic_terminate(event):
    if event.keysym == 'Up':

        startGame(event)
        # set up sound
        pygame.mixer.init()
        pygame.mixer.music.load('mega_man.wav')
        pygame.mixer.music.play(-1, 0.0)
        g_canvas.create_text(1300,420, text='Sound: ', fill='white', font=('fixedsys', 10))
        g_canvas.create_text(1300,435, text='ON = LEFT ARROW', fill='Green', font=('fixedsys', 10))
        g_canvas.create_text(1300,450, text='OFF = RIGHT ARROW', fill='Red', font=('fixedsys', 10))


    
    if event.keysym == 'Left':

        # plays the music back  
        pygame.mixer.init()
        pygame.mixer.music.load('mega_man.wav')
        pygame.mixer.music.play(-1, 0.0)
            
    if event.keysym == 'Right':
        
        # stops the music
        pygame.mixer.quit()

    if event.keysym == 'Escape':

        #terminates the program
        g_window.destroy()

        #pygame.mixer.quit()
        sys.exit()


# GUI

# create a GUI window 
g_window = Tk() 


# set the title 
g_window.title("Type Travel")


# dimensions
HEIGHT = 480
WIDTH = 1400
m_y = HEIGHT/2
m_x = WIDTH/2


# game canvas
g_canvas = Canvas(g_window,width=WIDTH, height=HEIGHT, bg='Black')
g_canvas.pack()


# game Title
g_canvas.create_text(1350, 10, text = "Type Travel",fill='white', font = ('fixedsys', 12)) 
g_canvas.pack() 


# create sprite
sprite1 = ImageTk.PhotoImage(Image.open('sprite1.png'))
sprite11 = g_canvas.create_image(10,10, image=sprite1)


# start game position
start_pos_x = 20
start_pos_y = 370

g_canvas.move(sprite11,start_pos_x,start_pos_y)


# sprite variable
sprite_vel = 20
g_canvas.pack()


# create planets
earth1 = ImageTk.PhotoImage(Image.open('earth.png'))
earth11 = g_canvas.create_image(50,55, image=earth1)

mars1 = ImageTk.PhotoImage(Image.open('mars.png'))
mars11 = g_canvas.create_image(50,55, image=mars1)

jupiter1 = ImageTk.PhotoImage(Image.open('jupiter.png'))
jupiter11 = g_canvas.create_image(50,55, image=jupiter1)

saturn1 = ImageTk.PhotoImage(Image.open('saturn.png'))
saturn11 = g_canvas.create_image(50,55, image=saturn1)

uranus1 = ImageTk.PhotoImage(Image.open('uranus.png'))
uranus11 = g_canvas.create_image(50,55, image=uranus1)

neptune1 = ImageTk.PhotoImage(Image.open('neptune.png'))
neptune11 = g_canvas.create_image(50,55, image=neptune1)


# create stars
star1 = ImageTk.PhotoImage(Image.open('stars.png'))
star11 = g_canvas.create_image(200,45, image=star1)

star2 = ImageTk.PhotoImage(Image.open('stars.png'))
star22 = g_canvas.create_image(700,45, image=star1)

star3 = ImageTk.PhotoImage(Image.open('stars.png'))
star33 = g_canvas.create_image(1200,45, image=star1)



# planet positions
g_canvas.move(earth11, 70, 160)
g_canvas.move(mars11, 250, 170)
g_canvas.move(jupiter11, 600, 230)
g_canvas.move(saturn11, 810, 240)
g_canvas.move(uranus11, 1010, 180)
g_canvas.move(neptune11, 1200, 194)


# add a score label 
scoreLabel = Label(g_window, text = "Score: ", font = ('fixedsys', 20))

scoreLabel.pack() 


# add a time left label 
timeLabel = Label(g_window, text = "Time left: " + str(timeleft), font = ('fixedsys', 20)) 
				
timeLabel.pack() 


# add a label for displaying the text
label = Label(g_window, font = ('fixedsys', 60)) 
label.pack() 


# add a text entry box
e = Entry(g_window, font=('Arial', 20)) 


# game introduction
starting_1 = g_canvas.create_text(m_x, m_y-120, text='Type Travel: ', fill='white', font=('fixedsys', 30))
starting_2 = g_canvas.create_text(m_x, m_y+50, text='''- You have to correctly type as many words as you can, under a time limit
- Each word is worth 100 points
- A bonus time of 2 seconds is added to the timer for every correctly typed word
(only if you have a score of 800 or over)

Planet Milestones:       
Earth - 500 points
Mars - 1500 points

-- Further Planets --
Jupiter - 3000 points
Saturn - 4000 points
Uranus - 5000 points
Neptune - 6000 points
''', fill='white', font=('fixedsys', 15))
starting_3 = g_canvas.create_text(m_x, m_y+200, text='Press the "Up" key to start the game', fill='white', font=('fixedsys', 30))
starting_4 = g_canvas.create_text(m_x, m_y+160, text='*!Please make sure to adjust the volume before playing!*', fill='red', font=('fixedsys', 15))
g_canvas.pack()


# run the 'startGame' function when the enter key is pressed
g_window.bind('<Return>', startGame)

g_window.bind('<Key>', startMusic_terminate)

# updates the window
e.pack() 


# set focus on the entry box 
e.focus_set()



# start the GUI 
g_window.mainloop() 

