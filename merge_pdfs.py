#merging pdf
from PyPDF2 import PdfFileMerger
import os
pdfs = os.listdir('pdf_generated')
merger = PdfFileMerger()
for pdf in pdfs:
    merger.append('pdf_generated/'+pdf)
merger.write('pdf_mergedfile.pdf')
merger.close()
input('all pdf files merged in mergedfile.pdf, saved in same folder, press enter to close program')
