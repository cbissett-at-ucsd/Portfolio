

#sorry learning python after C++ put function up first just in case
import PyPDF2 
from reportlab.pdfgen.canvas import Canvas
def getFile_w_Watermark(filepath,watermarktext):

    #get the size  and orientation of the first page
    target = PyPDF2.PdfFileReader(open(filepath,"rb"))
    targetpg=target.getPage(0)
    targetRotation=targetpg.get('/Rotate') 
    dimensions=targetpg.mediaBox
    width=dimensions[2]
    height=dimensions[3]


    #make a new page for the watermark
    page = Canvas("watermark.pdf")

    fontsize=height/50
    page.setFont("Helvetica",fontsize)
    page.setFillColorRGB(255,0,0)

    if targetRotation==90:
        #awkward coordinate shift to get things into  the bottom of the page
        page.rotate(90)
        temp=-width
        width=height
        height=temp
        lengthoftext=fontsize*len(watermarktext)*3/5 #3/5 is approximately ratio of height to width
        page.drawString(width/4-lengthoftext/2,height+fontsize,watermarktext) #center at 1/4 of page, put at bottom
    else:
        lengthoftext=fontsize*len(watermarktext)*3/5 #3/5 is approximately ratio of height to width
        page.drawString(width/2-lengthoftext/2,fontsize, watermarktext) #center at 1/4 of page, put

    page.save()
    watermark = PyPDF2.PdfFileReader(open('watermark.pdf',"rb"))
    watermarkpg=watermark.getPage(0)

    out = PyPDF2.PdfFileWriter()

    for x in range(target.getNumPages()):
        #put watermark on first page
        if x==0:
            watermarkpg=watermark.getPage(0)
            targetpg=target.getPage(0)
            targetpg.mergePage(watermarkpg)
            out.addPage(targetpg)
        else:
            out.addPage(target.getPage(x))

    #so all documents are self contained
    if target.getNumPages()%2 >0:
        out.addBlankPage()

    out.write(open("temp.pdf", 'wb'))
    return PdfFileReader("temp.pdf",'rb')


# ------------------------------------------------ACTUAL PROGRAM -----------------------------------------------------------------
from PyPDF2 import PdfFileMerger, PdfFileReader
merger = PdfFileMerger()

print("keep in mind, this program takes a couple minutes to finish merging pdfs, wait for program to reply done in command line")

snInit=100
import csv
csvpath='PDFmerge.csv'
with open(csvpath, newline='') as csvfile:
    AdressList = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in AdressList:
        # program takes a column of ONLY FILE NAMES, NOTHING ELSE, NO HEADER FOR COLUMN, CELL (1,1) IS JUST A FILE NAME
        filename=row[0]
        print(filename)
        watermarkstring= "SN: A"+str(snInit) + "      11/13/2020"
        snInit=snInit+1
        temp = getFile_w_Watermark(filename, watermarkstring)
        merger.append(temp)

outputAdress="document-output.pdf"
print("\nworking on\n"+outputAdress)
merger.write(outputAdress)
merger.close()
print("\n\n!!!! done !!!!")