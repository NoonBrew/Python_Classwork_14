import docx

document = docx.Document('IT_Sample_Resume.docx')

for para in document.paragraphs:
    if 'python' in para.text.lower():
        print('A Python programmer!!')
    # print(para.text)
    if 'ethical hacking' in para.text.lower():
        print('An ethical Hacker!')


