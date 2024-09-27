from datetime import datetime
import pymupdf

#Dimensões do A4 width 612 x height 792 points
#O arquivo que será buscado tem que estar com o nome ML.pdf
doc = pymupdf.open("ML.pdf") # open document
page1 = doc[0] # get the 1st page of the document
page1.set_cropbox(pymupdf.Rect(30, 140, 290, 570))

page2 = doc[1] # get the 2st page of the document
page2.set_cropbox(pymupdf.Rect(2, 0, 590, 755))

doc.save("temp_ML.pdf")

doc1 = pymupdf.open()  # new empty PDF
page=doc1.new_page()  # new page in A4 format

# página superior
r1 = pymupdf.Rect(0, 0, page.rect.width, page.rect.height/2)

# página inferior
r2 = r1 + (0, page.rect.height/2, 0, page.rect.height/2)

src = pymupdf.open("temp_ML.pdf") 
page.show_pdf_page(r1, src, 0, rotate=90)
page.show_pdf_page(r2, src, 1, rotate=90)
doc1.save(str(datetime.now())"_ML.pdf")
