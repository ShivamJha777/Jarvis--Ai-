import PyPDF2
def pdfreader(pdf_name,start_page,limit):
        start_page = start_page - 1
        reader = PyPDF2.PdfReader(f'{pdf_name}.pdf')
        print(len(reader.pages))
        text = ''
        for i in range(start_page,limit):
                text += reader.pages[i].extract_text()
        return text
