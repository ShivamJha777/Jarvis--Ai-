import PyPDF2
import os
def pdfreader(path,start_file = True):
        if start_file:
            os.startfile(path)
        book = open(path,'rb')
        pdf = PyPDF2.PdfFileReader(book)
        pages = pdf.getNumPages()
        print("Number of pages:",pages)
        a = ''
        for i in range(pages):
                page = pdf.pages[i]
                content = page.extract_text()
                a += str(content)
        book.close()
        return a
