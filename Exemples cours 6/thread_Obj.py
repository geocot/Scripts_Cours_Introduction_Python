import threading, time


class Processus(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        i = 0
        while i<10:
            print(threading.current_thread())
            time.sleep(0.5)
            i+=1


p1 = Processus()
p2 = Processus()

p1.start()
p2.start()

p1.join()
p2.join()

print("Terminé")