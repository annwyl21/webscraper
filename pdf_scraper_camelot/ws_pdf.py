import camelot

file = './pdf_scraper/LSE_BP_2022.pdf'

tables = camelot.read_pdf(file)
tables