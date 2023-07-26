from pathlib import Path 
import io 
import PyPDF2 
import pytesseract
import ocrmypdf
from pdf2image import convert_from_path

path_data = Path().cwd()/'data/reports'
path_out =  Path().cwd()/'data/reports_txt'
path_out.mkdir(parents=True, exist_ok=True)


# Traverse through all subfolders and process PDF files
for path_pdf_file in path_data.rglob('*.pdf'):
    file_stem = path_pdf_file.stem


    try:
        text = ''

        # Read PDF file and extract text 
        with open(path_pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            
            for page in range(num_pages):
                text += reader.pages[page].extract_text()
 

        # If extraction failed - try to convert pdf into image and extract text from image 
        if text.strip() == '':
            # Convert pdf into images and extract text from images
            images = convert_from_path(path_pdf_file, dpi=300, grayscale=True)
            for image in images:
                text += pytesseract.image_to_string(image, lang='deu', config='--psm 4')

            # with io.BytesIO() as output_stream:
            #     ocrmypdf.ocr(path_pdf_file, output_file=output_stream, language='deu', image_dpi=300, 
            #                   rotate_pages=True, deskew=True, remove_background=True, clean_final=True, 
            #                   tesseract_config='--psm 4',  force_ocr=True) #  redo_ocr=True,
            #     reader = PyPDF2.PdfReader(output_stream)
            #     for page in range(len(reader.pages)):
            #         text += reader.pages[page].extract_text()

        
        # Remove empty lines
        text = '\n'.join([line for line in text.split('\n') if line.strip() != ''])

        # Save text file 
        path_txt_file = path_out/f'{file_stem}.txt'
        with open(path_txt_file, 'w') as txt_file:
            txt_file.write(text)

        print(f"Processed {file_stem}")

    except Exception as e:
        print(f"Error processing {file_stem}: {e}")
