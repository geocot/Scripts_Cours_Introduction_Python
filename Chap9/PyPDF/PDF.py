from PyPDF2 import PdfReader, PdfWriter, PdfMerger

fichier = "Un fichier PDF.pdf"
#Ouverture du fichier
document = PdfReader(open(fichier, 'rb'))
#Lire les métadonnées
metedata = document.metadata
print(metedata)
#Pour obtenir le nombre de pages
print(len(document.pages))
#Pour lire le texte dans les pages
for page in range(0,len(document.pages)):
    laPage = document.pages[page]
    print(laPage.extract_text().replace('\n', ''))

#Pour la création de fichier
#Création d'une instance de PDFWriter
pdf_writer = PdfWriter()
#On ajoute des page
page = document.pages[0]
#On peut en faire la rotation
page.rotate(90)
#Ajout des pages dans le document
pdf_writer.add_page(page)
#Sauvegarde du document
pdf_writer.write("sortie.pdf")

#Assemblage
#Création de l'instance de PdfMerger()
pdf_merger = PdfMerger()
#Liste des documents à assembler
listePDF = ["sortie.pdf","Un fichier PDF.pdf" ]
#Ouvre les fichiers un à un
for pdf in listePDF:
    fichierPDFTempo = open(pdf, "rb")
    pdf_merger.append(fichierPDFTempo)
#Ouverture pour la sauvegarde
fichierPDF = open("assemblage.pdf", "wb")
#Ecriture
pdf_merger.write(fichierPDF)


