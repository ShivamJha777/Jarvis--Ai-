def agent(pdf_name,start_page,end_page,question):
    import PyPDF2
    reader = PyPDF2.PdfReader(f'{pdf_name}.pdf')
    a = ''
    for i in range(start_page, end_page):
        page = reader.pages[i]
        content = page.extract_text()
        a += str(content)
    import g4f

    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user",
                   "content": f"{a}\nStrictly Based on the above data answer the question:{question}"}],
    )
    return response
