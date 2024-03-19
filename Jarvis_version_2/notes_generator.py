def pdf_notes(pdf_name,start_page,end_page,word_per_point):
    import PyPDF2
    import time
    import pyautogui
    reader = PyPDF2.PdfReader(f'{pdf_name}.pdf')
    a = ''
    for i in range(start_page,end_page):
        page = reader.pages[i]
        content = page.extract_text()
        a += str(content)
    import g4f

    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{a}\n Make vivid notes on the above data each point should have atleast {word_per_point} words"}]
    )
    response = response.replace('#','')
    pyautogui.press('super')
    time.sleep(0.4)
    pyautogui.write('Word')
    time.sleep(0.9)
    pyautogui.press('enter')
    time.sleep(2.7)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(f'{response}')
    return 'Notes typed in a word document'