import re
import random
import os

def download(url,
             target_filename,
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # imports the function for opening website and the class for creating requests
    from urllib.request import urlopen, Request

    # opens the website for reading
    request = url
    web_page = urlopen(request)

    #decodes the content of the site as a character string
    web_page_contents = web_page.read().decode(char_set)

    #optionally copies the contents to a text file
    if save_file:
        text_file = open(target_filename + '.' + filename_extension,
                            'w', encoding = char_set)
        text_file.write(web_page_contents)
        text_file.close()
    
    return web_page_contents
    
#asks user for website link, downloads and opens site
x = ('https://' + input("Enter website url: "))
download(x, 'thewebsite')
openre = open('thewebsite.html', 'r', encoding="utf-8")
readpage = openre.read()

#removes all website data that is not a digit, randomly selects 3000 of these strings and joins them into 1 long string
allnumbers = re.findall(r'\d+', readpage)
randomnumbers = random.choices(allnumbers, k=3000)
longseed = ''.join(randomnumbers)

#shortens the long string into 3000 digits in length, divides it into 3 digit numbers, converts all numbers to integers
shortseed = longseed[:3000] + (longseed[3000:] and '')
n = 3
finalseed = [shortseed[i:i+n] for i in range(0, len(shortseed), n)]
listofintegers = list(map(int, finalseed))

#injects integers into processing code template, asks for file name, determines the users desktop location based on their os, runs the processing code
thecode = 'app = App({}, {});app.background({}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.stroke({}, {}, {});app.strokeWeight({});app.line({}, {}, {}, {});app.redraw();app.saveFrame(savelocation)'.format(*listofintegers)
filename = input("Enter a title for your art: ")
operatingsystem = input("What operating system are you using? W/M/L: ")
if operatingsystem == 'W':
    savelocation = (fr"C:\Users\{os.getlogin()}\Desktop\{filename}.png")
else :
    savelocation = (fr"~/Desktop/{filename}.png")
from processing_py import *
exec(thecode)
