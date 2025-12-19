from urllib.request import urlopen
from urllib.parse import urljoin
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
        counter = 0
        print(url)
        for link in neededLinks: #Logic to find link to price pages, might be removed l8r
            Inhref = link.get('href')
            textL = link.text.lower()
            keywords = ["preis", "pric", "dienst", "servic", "behandl", "leist"]
            if any(keyword in textL for keyword in keywords):
                priceUrl = urljoin(url, Inhref)
                priceHtml = urlopen(priceUrl).read()
                priceSoup = BeautifulSoup(priceHtml, "html.parser")
                neededPrice = priceSoup.find_all()
                for counter, prices in enumerate(neededPrice): #Logic to get prices
                    if "€" in prices.text:
                        try:
                            print(neededPrice[counter - 1].text)
                            print(neededPrice[counter].text)
                            print(neededPrice[counter + 1].text)
                        except:
                            continue
                    else:
                        continue
                break
                print("----------")
            else:
                continue
    except:
        print("Invalid link")
        continue
