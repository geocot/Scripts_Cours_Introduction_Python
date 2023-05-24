import zipfile
fichier = "creationfichiers.zip"
fichierZip = zipfile.ZipFile(fichier, 'r')
fichierZip.extract("test/fichierZip.py",r"C:\temp\PythonMai\extr")
fichierZip.close()



