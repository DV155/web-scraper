from urllib.request import urlopen
from bs4 import BeautifulSoup

#Code requires local file with the data
fileName = input("Enter file name:")
fhand = open(fileName)
for line in fhand:
    try:
        url = line.rstrip()
        html = urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
    except:
        print("Invalid link")
        continue
