from PyPDF2 import PdfWriter #Import the PdfWriter class from the PyPDF2 library.

merger = PdfWriter() #Create a PdfWriter object called merger, which will combine the PDFs.

for pdf in ["sample-1.pdf", "sample-2.pdf",]: #Loop through a list of PDF filenames (sample-1.pdf and sample-2.pdf).
    merger.append(pdf) #Append each PDF file to the merger object.

merger.write("merged-pdf.pdf") #Write the merged PDF to a new file called "merged-pdf.pdf".
merger.close() #Close the merger to free up resources.






