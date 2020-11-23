

from PyPDF2 import PdfFileMerger, PdfFileReader
merger = PdfFileMerger()
blank = PdfFileReader("U:/Staff/Christian B/codedprograms/Python/pdf merge/blank.pdf",'rb') #MUST HAVE BLANK PAGE SAVED AS BLANK PDF IN FOLDER 


print("keep in mind, this program takes a couple minutes to finish merging pdfs, wait for program to reply done in command line")


import csv
with open('U:/Staff/Christian B/codedprograms/Python/pdf merge/PDFmerge.csv', newline='') as csvfile:
    AdressList = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in AdressList:
        # program takes a column of ONLY FILE NAMES, NOTHING ELSE, NO HEADER FOR COLUMN, CELL (1,1) IS JUST A FILE NAME
        print(row[0])
        filename=' '.join(row)
        #print(filename)
        temp = PdfFileReader(filename,'rb')
        merger.append(temp)

        #makes new documents start on fresh page
        isodd= temp.getNumPages()
        isodd=int( isodd % 2 )
        if isodd > 0 :
            merger.append(blank)

print("\nworking on\nU:/Staff/Christian B/codedprograms/Python/pdf merge/document-output.pdf")
merger.write("U:/Staff/Christian B/codedprograms/Python/pdf merge/document-output.pdf")
merger.close()
print("\n\n!!!! done !!!!")