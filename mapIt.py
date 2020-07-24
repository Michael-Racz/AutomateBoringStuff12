#mapIt.py

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    #get Address from command Line
    addres = ' '.join(sys.argv[1:])
else:
    #TODO: Get address from clipboard
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)