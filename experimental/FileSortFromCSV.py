

from shutil import copyfile
#copyfile(src, dst)

#set up directory
DstDir =    "U:/Staff/Christian B/codedprograms/Python/" #destination directory
CableDir=   DstDir + "CableAssy/"
VidDir=     DstDir + "COTs-VIDs/"
LabelDir=   DstDir + "Labels/"
MetalDir=   DstDir + "MetalParts/"
#circuit card? 
#assembaly?

SourceDir = "U:/Staff/Christian B/codedprograms/Python/"

CsvPath =   "U:/Staff/Christian B/codedprograms/Python/"

#start reading file names from csv and their paired classification
#must be in format
# filename.pdf , commodity type
# NO HEADERS IN FILE

import csv
with open(CsvPath, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        commodity= row[1]
        filename= row[0]

        '''
        src= SourceDir + filename
        if commodity == "CABLE" :
            dst= CableDir + filename
            copyfile(src, dst)

        if commodity == "VID" :
            dst= VidDir + filename
            copyfile(src, dst)
            
        if commodity == "LABEL" :
            dst=LabelDir + filename 
            copyfile(src, dst)

        if commodity == "METAL PART" :
            dst=MetalDir + filename
            copyfile(src, dst)
        '''
        



