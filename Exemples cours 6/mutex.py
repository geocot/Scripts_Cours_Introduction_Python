import threading, time
lock = threading.RLock()

class Procedure(threading.Thread):
    def __init__(self, mot):
        threading.Thread.__init__(self)
        self._mot = mot

    def run(self):
        with lock:
            for l in self._mot:
                    print(l)
                    time.sleep(0.3)

p1 = Procedure("Soleil")
p2 = Procedure("Pluie")
p3 = Procedure("Neige")


p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()
