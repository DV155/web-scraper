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
        neededLinks = soup.find_all('a')
        for link in neededLinks:
            Inhref = link.get('href')
            textL = link.text.lower()
            keywords = ["preis", "pric", "dienst", "servic", "behandl"]
            if any(keyword in textL for keyword in keywords):
                priceUrl = Inhref
                priceHtml = urlopen(priceUrl).read()
                priceSoup = BeautifulSoup(priceHtml, "html.parser")
            else:
                continue

    except:
        print("Invalid link")
        continue
