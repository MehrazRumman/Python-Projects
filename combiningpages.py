#! python3
# combines all the pdfs in the current working directory into a single pdf
import PyPDF2, os
# get all the pdf filenames .
pdffiles=[]
for filename in os.listdir("d:\\"):
    if filename.endswith(".pdf"):
        pdffiles.append(filename)
pdffiles.sort(key=str.lower)
pdfwriter=PyPDF2.PdfFileWriter()
# TODO: loop through all the pdf files
for filename in pdffiles:
    pdffileobj=open(filename,"rb")
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    # todo: loop through all the pages (except the first) and add them
    for pagenum in range(1,pdfreader.numPages):
        pageobj=pdfreader.getPage(pagenum)
        pdfwriter.addPage(pageobj)
# todo: save the resulting pdf to a file
pdfoutput=open("allminutes.pdf","wb")
pdfwriter.write(pdfoutput)
pdfoutput.close()



