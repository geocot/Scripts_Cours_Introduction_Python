import bs4 as bs
import urllib.request
import time

class Meteo:
    "Lecteur de météo en format XML"
    def __init__(self, lienURL):
        self._lienURL = lienURL
        self._messageMeteo = ""
    def getMeteo(self):
        self._lireXML()
        return self._messageMeteo

    def _lireXML(self):
        try:
            avertissement = ''
            url = self._lienURL
            req = urllib.request.urlopen(url).read()
            soup = bs.BeautifulSoup(req, 'lxml')
            for titre in soup.find_all('title'):
                if titre.text.count("Conditions") > 0:
                    txtMeteo = titre.text.split(':')[1].strip().replace("°C", "")
                    txtMeteo = txtMeteo.replace(",", " *", 1)
                if titre.text.count("AVERTISSEMENT") > 0:
                    avertissement =  " : ***" + titre.text.split(',')[0] + "***"
            localtime = time.asctime(time.localtime(time.time()))
            self._messageMeteo =  localtime + ' ' + txtMeteo + avertissement


        except Exception as e:
            self._messageMeteo = 'Oups un problème...' + e


if __name__ == '__main__':
 m = Meteo('https://meteo.gc.ca/rss/city/qc-147_f.xml')
 print(m.getMeteo())

