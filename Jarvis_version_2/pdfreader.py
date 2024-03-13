import PyPDF2
reader = PyPDF2.PdfReader('Atomic habits ( PDFDrive ).pdf')
def pdfreader(start_page,limit = len(reader.pages)):
        start_page = start_page - 1
        reader = PyPDF2.PdfReader('Atomic habits ( PDFDrive ).pdf')
        print(len(reader.pages))
        text = ''
        for i in range(start_page,limit):
                text += reader.pages[i].extract_text()
        return text
