    #get size of first page
import PyPDF2 
from reportlab.pdfgen.canvas import Canvas

target = PyPDF2.PdfFileReader(open("vid.pdf","rb"))
targetpg=target.getPage(0)
targetRotation=targetpg.get('/Rotate') #is page normal or in landscape, normal=0 landscape=90
dimensions=targetpg.mediaBox
width=dimensions[2]
height=dimensions[3]


x=100
prefix="A"
sn= prefix+ str(x)

#make a new page for the watermark

page = Canvas("x.pdf")

fontsize=height/50
page.setFont("Helvetica",fontsize)
page.setFillColorRGB(255,0,0)
if targetRotation==90:
    #awkward coordinate shift to get things into  the bottom of the page
    page.rotate(90)
    temp=-width
    width=height
    height=temp
    outputstring="SN: A100"
    lengthoftext=fontsize*len(outputstring)*3/5 #3/5 is approximately ratio of height to width
    page.drawString(width/4-lengthoftext/2,height+fontsize/2,outputstring) #center at 1/4 of page, put at bottom

if targetRotation==0:
    outputstring="SN: A100"
    lengthoftext=fontsize*len(outputstring)*3/5 #3/5 is approximately ratio of height to width
    page.drawString(width/2,0, outputstring) #center at 1/4 of page, put at bottom


page.save()

#move the page into pypdf to add it as a watermark
watermark = PyPDF2.PdfFileReader(open('x.pdf',"rb"))

watermarkpg=watermark.getPage(0)

out = PyPDF2.PdfFileWriter()

for x in range(target.getNumPages()):
    if x==0:
        watermarkpg=watermark.getPage(0)
        targetpg=target.getPage(0)
        targetpg.mergePage(watermarkpg)
        out.addPage(targetpg)
    else:
        out.addPage(target.getPage(x))
if target.getNumPages()%2 >0:
    out.addBlankPage()

out.write(open("output.pdf", 'wb'))
