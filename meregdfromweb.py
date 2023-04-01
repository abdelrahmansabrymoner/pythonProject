import requests
import io
import base64
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Replace with your Google Form link
form_link = 'https://docs.google.com/forms/d/e/1FAIpQLSd6gF_BuJJAgpGBJWsdAq8u8cxmZv6Rda5cndpAjwFHHxe6qQ/viewscore?viewscore=AE0zAgDVxANXgVikquCa88DxsjhKJRcUpfuQyrwCaZKItmIfRWt3P4YdpcFL491CyGzkhew'

# Retrieve the form responses as CSV data
response = requests.get(form_link + '/formResponse')
csv_data = response.content.decode('utf-8')

# Create a PDF file containing the form response data
pdf_file_name = 'form-responses.pdf'
pdf_file = canvas.Canvas(pdf_file_name, pagesize=letter)
textobject = pdf_file.beginText()
textobject.setTextOrigin(72, 720)
for row in csv_data.split('\n'):
    for col in row.split(','):
        textobject.textLine(col.strip())
pdf_file.drawText(textobject)
pdf_file.save()

# Print the base64-encoded PDF file content
with open(pdf_file_name, 'rb') as f:
    pdf_bytes = f.read()
pdf_b64_bytes = base64.b64encode(pdf_bytes)
pdf_b64_str = pdf_b64_bytes.decode('utf-8')
print(pdf_b64_str)
