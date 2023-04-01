import os
from PyPDF2 import PdfMerger

file_name = input("Enter the file name with extention: ")
# specify the directory where the PDF files are located
directory = 'E:\Second Year\Second Term\CCNA\Lecature\ccna ques'

# initialize a PdfMerger object
pdf_merger = PdfMerger()

# loop through all PDF files in the directory and add them to the merger
for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        filepath = os.path.join(directory, filename)
        pdf_merger.append(open(filepath, 'rb'))

# write the merged PDF to a file
with open(file_name, 'wb') as output_file:
    pdf_merger.write(output_file)

# close all input PDF files
pdf_merger.close()
