import urllib.request
import bs4

lienImage = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.atom"

page = urllib.request.urlopen(lienImage)
xml = bs4.BeautifulSoup(page,'lxml')
e = xml.find_all('title')
for eq in e:
    print(eq)