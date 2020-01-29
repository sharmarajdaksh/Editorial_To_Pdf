import subprocess
import os
import re

from get_article import get_article_TH, get_article_IE

# Hardcoded URLs for testing
url = "https://indianexpress.com/article/opinion/editorials/kumaraswamy-upa-congress-jds-karnataka-elections-5741258/"
filename = "IE"

def save_article_as_pdf(url, filename):

    # Save text as a docx
    if (re.search("indianexpress.com", url)):
        get_article_IE(url, filename)
    else:
        get_article_TH(url, filename)

    # Convert the docx to pdf
    subprocess.call("pandoc {}.docx --pdf-engine=pdflatex.exe -o {}.pdf".format(filename, filename))

    # Remove the docx
    os.remove(filename + '.docx')