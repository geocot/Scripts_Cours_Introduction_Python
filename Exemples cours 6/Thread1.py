import threading, time

def afficheA():
    i = 0
    while i<10:
        print('a')
        time.sleep(0.3)
        i+=1

def afficheB():
    i = 0
    while i<10:
        print('b')
        time.sleep(0.3)
        i+=1

a = threading.Thread(target=afficheA, name="Thread A") #Sans les parenthèses.
b = threading.Thread(target=afficheB,  name="Thread B")

a.start()
b.start()
print(threading.enumerate())
a.join()
b.join()

print("Terminé")