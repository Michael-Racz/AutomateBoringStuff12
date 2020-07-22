#2048.py
#write a program that will open the game at https://play2048.co/ and keep sending up right down left keystrokes to autoamtically play the game

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pandas import DataFrame
import matplotlib.pyplot as plt
browser = webdriver.Firefox()
browser.get('https://play2048.co/')
score_list =[]
experiment_dict ={'Experiment #': [1,2,3,4,5,6,7,8,9,10]}


keySend = browser.find_element_by_tag_name('html')
#Used to tell if the game has shown the "GAME OVER" text
gameOverText = browser.find_element_by_css_selector('.game-message > p:nth-child(1)')
#Used to click New Game
newGameButton = browser.find_element_by_css_selector('.restart-button')
#Access the score of the game
scoreBox = browser.find_element_by_class_name('score-container')

#TODO: Try different patterns or let the user pick from a set of patterns
i = 0
while True and i < 10:

   keySend.send_keys(Keys.UP)
   #time.sleep(.1)
   keySend.send_keys(Keys.RIGHT)
   #time.sleep(.1)
   keySend.send_keys(Keys.DOWN)
   #time.sleep(.1)
   keySend.send_keys(Keys.LEFT)
   #time.sleep(.1)
   
   #If the GAME OVER screen is triggered, and a way to reset the game(Click 'New Game')
   #isdisplayed returns true if the element is visible, false otherwise
   if gameOverText.is_displayed():
      #Prints out the game's score before proceeding to the new game.
      #TODO: Use for graphing the scores
      #print(scoreBox.text)
      i += 1
      score_list.append(int(scoreBox.text))
      newGameButton.click()

experiment_dict.setdefault('Score',score_list)
df = DataFrame(experiment_dict, columns = ['Score','Experiment #'])
df.plot(x = 'Experiment #', y ='Score',kind = 'scatter')
plt.show()
