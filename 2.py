import PyPDF2
pdf_file = open('f.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
document_text = ''
for page in pdf_reader.pages:
    document_text += page.extract_text()

print(document_text)
while True:
    customer=input('you:')
    if customer.__contains__('faizer'):
        print('chatbot:',document_text)
    else :
        print('chatbot:sorry!! data is not feeded')