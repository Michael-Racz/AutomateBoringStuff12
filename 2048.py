#2048.py

#write a program that will open the game at https://play2048.co/ and keep sending up right down left keystrokes to autoamtically play the game

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('https://play2048.co/')

keySend = browser.find_element_by_tag_name('html')


while True:
   keySend.send_keys(Keys.UP)
   time.sleep(.1)
   keySend.send_keys(Keys.RIGHT)
   time.sleep(.1)
   keySend.send_keys(Keys.DOWN)
   time.sleep(.1)
   keySend.send_keys(Keys.LEFT)
   time.sleep(.1)
