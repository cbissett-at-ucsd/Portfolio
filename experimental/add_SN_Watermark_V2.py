#get size of first page
import PyPDF2 
target = PyPDF2.PdfFileReader(open('wideboi.pdf',"rb"))
dimensions=target.getPage(0).mediaBox
width=dimensions[2]
height=dimensions[3]

print(dimensions)

x=100
prefix="A"
sn= prefix+ str(x)

#make a new page for the watermark
from reportlab.pdfgen.canvas import Canvas
page = Canvas("x.pdf")

fontsize=height/50
page.setFont("Helvetica",fontsize)
page.setFillColorRGB(255,0,0)

#awkward coordinate shift to get things into  the bottom of the page
page.rotate(90)
temp=-width
width=height
height=temp
outputstring="SN:" + sn 
lengthoftext=fontsize*len(outputstring)*3/5 #3/5 is approximately ratio of height to width
page.drawString(width/4-lengthoftext/2,height+fontsize/2,outputstring) #center at 1/4 of page, put at bottom


page.save()

#move the page into pypdf to add it as a watermark
watermark = PyPDF2.PdfFileReader(open('x.pdf',"rb"))

watermarkpg=watermark.getPage(0)

out = PyPDF2.PdfFileWriter()

for x in range(target.getNumPages()):
    if x%2==0:
        watermarkpg=watermark.getPage(0)
        targetpg=target.getPage(x)
        targetpg.mergePage(watermarkpg)
        out.addPage(targetpg)
    else:
        out.addPage(target.getPage(x))


out.write(open("output.pdf", 'wb'))