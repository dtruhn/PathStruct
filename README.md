# HistopathAIzer
\
Install
=============
Depending on your setup you have to install the following:\
`sudo apt-get install tesseract-ocr`

Create virtual environment and install packages: \
`python -m venv venv` \
`source venv/bin/activate`\
`pip install -e .`

\
Get Started 
=============

1  ChatGPT API Key
-------------------
* create a file `secret_api_key.txt` in the root folder (next to this file) and copy your secret API key inside

2 Prepare data
-------------
* place all your pdf-files under `data/reports` 

3 Extract text from data 
------------
* Run [scripts/pdf2text.py](scripts/pdf2text.py)

4 Create structured report from text 
-----------------
* Run [scripts/text2report.py](scripts/text2report.py)
