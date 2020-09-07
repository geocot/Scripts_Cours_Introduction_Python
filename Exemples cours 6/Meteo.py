
import time, string
import urllib.request
import bs4 as bs

while 1:
    try:
        f = open(r'c:\temp\meteo.txt', 'a')
        url = 'https://meteo.gc.ca/rss/city/qc-133_f.xml'
        req = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(req, 'lxml')
        txtMeteo = ""
        for titre in soup.find_all('title'):
            if titre.text.count("Conditions") > 0:
                txtMeteo = titre.text.split(':')[1].strip().replace("°C", "")
                txtMeteo = txtMeteo.replace(",", " *", 1)
            if titre.text.count("AVERTISSEMENT") > 0:
                print("***" + titre.text.split(',')[0] + "***")
        localtime = time.asctime(time.localtime(time.time()))
        print(localtime + ' ' + txtMeteo)
        f.write(localtime + ' ' + txtMeteo + "\n")

    except Exception as e:
        print(str(e))
        pass
    finally:
        f.close()

    time.sleep(600)
