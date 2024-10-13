from datetime import datetime
import pymupdf

#Dimensões do A4 width 612 x height 792 points
#O arquivo que será buscado tem que estar com o nome Shopee.pdf
doc = pymupdf.open("Shopee.pdf") # open document
page1 = doc[0] # get the 1st page of the document
page1.set_cropbox(pymupdf.Rect(0, 0, 310, 410))
page2 = doc[1] # get the 2st page of the document
page2.set_cropbox(pymupdf.Rect(2, 0, 580, 551))
#Aqui Criaremos um arquivo temporário com os cortes na página 1 e na página 2
doc.save("Temp_Shopee.pdf")

doc = pymupdf.open()  # Aqui criamos um novo PDF vazio
page=doc.new_page()  # Definimos o formato A4

# página superior
r1 = pymupdf.Rect(0, 0, page.rect.width, page.rect.height/2)

# página inferior
r2 = r1 + (0, page.rect.height/2, 0, page.rect.height/2)

src = pymupdf.open("Temp_Shopee.pdf") 
page.show_pdf_page(r1, src, 0, rotate=90)
page.show_pdf_page(r2, src, 1, rotate=90)
#Inclui uma string com data, e renomear o novo PDF,  para não escrever por cima do arquivo anterior.
doc.save(str(datetime.now())+"_Shopee.pdf")
