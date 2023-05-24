import serial, time
ser = serial.Serial('COM7')  # ouverture du port
print(ser.name)         # Impression du port utilisé dans la console
try:
    while 1:
        ligne = ser.readline() #Lecture des informations sur le port
        print(ligne) #Affichage de la lecture
        time.sleep(1) #Attente de 1 seconde
except e as Exception:
    print(e)
    ser.close()             # Fermeture du port

    