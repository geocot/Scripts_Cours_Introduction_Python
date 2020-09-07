import threading, time, objMeteo

def affiche(url, ville):
    m = objMeteo.Meteo(url)
    i = 0
    while i<10:
        print(ville, m.getMeteo())
        time.sleep(1)
        i+=1

a = threading.Thread(target=affiche, args=('https://meteo.gc.ca/rss/city/qc-133_f.xml','Québec'))
b = threading.Thread(target=affiche, args=('https://meteo.gc.ca/rss/city/qc-147_f.xml','Montréal'))

a.start()
b.start()

a.join()
b.join()

print("Terminé")