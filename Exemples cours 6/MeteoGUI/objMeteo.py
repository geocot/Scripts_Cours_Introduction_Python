import bs4 as bs
import urllib.request
import time
import warnings
warnings.filterwarnings('ignore', category=bs.builder.XMLParsedAsHTMLWarning)

class Meteo:
    "Lecteur météo en format XML"
    def __init__(self, lienURL):
        self._lienURL = lienURL
        self._condition = ""
        self._temperature = ""
        self._tendanceTemperature = ""
        self._pression=""
        self._tendancePression=""
        self._avertissement = ""
        self._dateHeure = ""
        self._ancienneLectureTemperature = 0

    def lireMeteo(self):
        self._lireXML()
        self._dateHeure = time.asctime(time.localtime(time.time()))
        temperature = float(self._temperature.replace("°C", "").replace(",", "."))
        if  temperature > self._ancienneLectureTemperature:
            self._tendanceTemperature = "hausse"
        elif temperature< self._ancienneLectureTemperature:
            self._tendanceTemperature = "baisse"
        else:
            self._tendanceTemperature = self._tendanceTemperature

        self._ancienneLectureTemperature = temperature

    @property
    def condition(self):
        return self._condition
    @property
    def temperature(self):
        return self._temperature
    @property
    def pression(self):
        return self._pression
    @property
    def tendancePression(self):
        return self._tendancePression
    @property
    def avertissement(self):
        return self._avertissement
    @property
    def dateHeure(self):
        return self._dateHeure
    @property
    def tendanceTemperature(self):
        return self._tendanceTemperature

    def _lireXML(self):
        try:
            url = self._lienURL
            req = urllib.request.urlopen(url).read()
            soup = bs.BeautifulSoup(req, 'lxml')
            categories = soup.find_all('category')
            sommaire = soup.find_all('summary')
            title = soup.find_all('title')
            for n, categorie in enumerate(categories):
                if categorie.attrs['term']=="Conditions actuelles":
                    sansBold = str(sommaire[n]).replace("<b>","").replace("</b>", "").split("<br/>")
                    for item in sansBold:
                        if item.count('Condition')>0:
                            self._condition = item.split(":")[1].strip()
                        if item.count('Température') > 0:
                            self._temperature = item.split(":")[1].strip()
                        if item.count('Pression') > 0:
                            self._pression = item.split(":")[1].split("kPa")[0].strip()
                            self._tendancePression = item.split("la")[1].strip()

            avertissementTrouve = False
            for n, titre in enumerate(title):
                if titre.text.count("AVERTISSEMENT") > 0:
                    self._avertissement = titre.text.split(',')[0]
                    avertissementTrouve = True
            if avertissementTrouve == False:
                self._avertissement = ""

        except Exception as e:
            print('Oups un problème...' + str(e))



if __name__ == '__main__':
 m = Meteo('https://meteo.gc.ca/rss/city/qc-133_f.xml')
 m.lireMeteo()
 print(m.condition, m.temperature)
