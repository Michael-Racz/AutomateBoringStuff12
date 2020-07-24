# AutomateBoringStuff12
Chapter 12 projects from Web Scraping

## 2048abridged.py
This program is an extension of the 2048.py mentioned below. This program will use selenium to open a firefox browser to play the game 2048 automatically. The program specifically uses the same button presses repeated (UP, RIGHT, DOWN, LEFT). On a game over the program will store the score and click the "new Game" button. 

This was quite an achievement to watch the program constantly loop on the game and run possibly forever. I limited it to only run 10 times and wanted to implement some use of the matplotlib library. So the program stores the scores of 10 games and plots them in a scatter plot after the 10 games have run. I also took out the user friendly timer to make it easier to see. I thought that having it complete the 10 games as fast as possible would be more enjoyable to see the graph result. If you would like to see more games, change NUM_GAMES.


## 2048.py
This program will open a web browser in firefox and start playing the game 2048 with repeated keypresses: UP, RIGHT, DOWN, LEFT. The game will not restart upon a game over. **For this program to work on your own you will need to use geckodriver for Firefox. Otherwise, you will not be able to open a window.**

### Uses
Selenium for the webdriver, selenium.webdriver.common.keys for the arrow key presses, and time for the program to slow down. It looks better when the presses are .1 seconds apart and not all instant.



Future plans with this project include:

-tracking different play styles to see which 'random' presses yield the highest scores.

-Being able to restart the game when there is a "Game Over"


## downloadXkcd.py
This program downloads every single Xkcd Comic from the website and puts them in a folder in the current working directiory. It uses the requests and beautiful soup module. There are over 2000 but I have included how to change it from it's current cap of 5 downloads to all of them. It also starts from the most recent and goes backwards.



