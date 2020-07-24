'''
Write a program that takes an email address and string of text on the command line and then, using selenium, logs in to your email account and sends an email of the string to the provided address. (You might want to set up a separate email account for this program.)

This would be a nice way to add a notification feature to your programs. You could also write a similar program to send messages from a Facebook or Twitter account.

This is a project from Automate The Boring Stuff Chapter 12.
'''
import sys,time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get(r'https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

your_email = YOUR EMAIL
your_password = YOUR PASSWORD

to_email = sys.argv[1]
subject = sys.argv[2]
text = ' '.join(sys.argv[3:])


def sendEmail():
    username = browser.find_element_by_id('identifierId')
    username.send_keys(your_email)
    username.send_keys(Keys.ENTER)
    time.sleep(2)
    passwordbox = browser.find_element_by_name('password')
    passwordbox.send_keys(your_password)
    passwordbox.send_keys(Keys.ENTER)
    time.sleep(3)
    Composebutton = browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div')
    Composebutton.click()
    time.sleep(2)
    browser.find_element_by_xpath("//textarea[@aria-label='To']").send_keys(to_email)
    browser.find_element_by_xpath("//input[@aria-label='Subject']").send_keys(subject)
    browser.find_element_by_xpath("//div[@aria-label='Message Body']").send_keys(text)
    browser.find_element_by_xpath("//div[@aria-label='Message Body']").send_keys(Keys.CONTROL,Keys.ENTER)
    print('Email sent.')

sendEmail()
