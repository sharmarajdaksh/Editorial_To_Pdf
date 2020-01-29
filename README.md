# Editorial to PDF script.

## What does the script do?

Basically, the script goes to the Editorial page of the websites of The Hindu, parses the HTML, and gets the URL for the listed articles. For each URL that it has, the program now fetches the article itself by parsing via BeautifulSoup, converts the HTML to .docx files for each article which are then converted to pdfs. I originally intended to also make it work for Editorials on the website of The Indian Express but later left that unimplemented.

## Dependencies?

There were quite a few depencies which were all installable via pip3. Please see imports in the python files to get an idea of the dependencies.
Besides the python packages, you'll also need to install [Pandoc](https://www.pandoc.org), an open source file converted and writing tool.

## Executing the script

To use the script, open the file fetch_urls_TH.py, configure the hardcoded variables such as file path to save the file to. Install any dependencies you see in the 3 python files (beutiful soup, docx, etc.), then just run the script using `python fetch_urls_TH.py`.
The script takes some time to execute since fetching the data, converting between file types, etc. take time. Wait for the script to finish executing and see the magic. :)

## Can you use it too?

I really don't know, to be honest. The website layouts may have changed since I made the script. Further, I only ran this script on my Windows system so OS compatibility issues such as directory structuring may need to be fixed if you intend to use the scripts.


