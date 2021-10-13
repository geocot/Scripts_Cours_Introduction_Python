import socket

host=""
port=5566

connexion_principale = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connexion_principale.bind((host,port))

print('le serveur est allumé')

while True:
    connexion_principale.listen(5)
    conn, address = connexion_principale.accept()
    print("Écoute!")
    data = conn.recv(1024)
    data = data.decode("utf8")
    print(data)





