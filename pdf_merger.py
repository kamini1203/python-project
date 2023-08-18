import PyPDF2



pdf_merger = PyPDF2.PdfMerger()
pdf_files_list = ['brain.pdf','dummy.pdf','ourEnvirpnment.pdf']

for pdf_file_name in pdf_files_list:
    with open(pdf_file_name, 'rb') as pdf_file:
        pdf_merger.append(pdf_file)

with open('Python_Tutorial_merged.pdf', 'wb') as pdf_file_merged:
    pdf_merger.write(pdf_file_merged)