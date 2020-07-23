#! python3
#downloadXkcd.py  - downloads every single XKCD comic.
#This program uses beautiful soup and the requests module to access a web browser and download every xkcd comic. Currently I have it set to download 5. See program to download all

import requests,os,bs4
url = 'https://xkcd.com' #starting url
os.makedirs('xkcd', exist_ok=True) #strore comics in ./xkcd
##
#Changed to '2328/' to only download 5 of the comics. To download all, Change '2328/' to '#'
##
while not url.endswith('2328/'):
    #TODO: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')

    #TODO: Find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem ==[]:
        print('Could not find the image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
    #TODO: Download the image
        print('Downloading image %s' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    #TODO: save the image to ./xkcd
        imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    #TODO:Get the prev buttons url
        prevLink = soup.select('a[rel="prev"]')[0]
        url= 'https://xkcd.com' + prevLink.get('href')
print('Done')
