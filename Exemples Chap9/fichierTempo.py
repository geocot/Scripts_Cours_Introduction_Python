import tempfile
temp = tempfile.TemporaryFile()
print(temp)
temp.write(b"Allo")
temp.seek(0)
print(temp.read().decode())
print(temp.name)
temp.close()


