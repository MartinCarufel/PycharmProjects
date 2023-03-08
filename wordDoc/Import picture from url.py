import io
import urllib.request
from docx import Document
from docx.shared import Inches

document = Document()
p = document.add_paragraph()
r = p.add_run()
url = r"https://uploads-ssl.webflow.com/6014e375fb2fcc14f5e89e9b/6182f2bb0222842cde8a264e_spirit-plane-p-1600.png"
io_url = io.BytesIO(urllib.request.urlopen(url).read())
r.add_picture(io_url)
document.save('demo.docx')