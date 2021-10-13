import socket, sys

host="localhost"
port=5566
connexion_principale = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    connexion_principale.connect((host,port))
    print("Connecté!")

    data = "Bonsoir!"
    data = data.encode("utf8")
    connexion_principale.sendall(data)
except ConnectionRefusedError:
    print("Oups!")
finally:
    connexion_principale.close()

