# -*- coding: utf-8 -*-
"""6stickanddotmedia9 task 5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mIOlgOcHY9irK4VaZbqiq81dVZkUFTfl
"""

!pip install pytesseract
!pip install pymupdf
!pip install fpdf

!apt-get install -y tesseract-ocr
!pip install pytesseract

import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from google.colab import files
import os

# 🟢 Upload Files (PDFs & Images)
uploaded = files.upload()

if not uploaded:
    print("❌ No files uploaded!")
else:
    extracted_text = ""

    for file_name in uploaded.keys():
        print(f"✅ Processing: {file_name}")

        # Check file extension
        ext = os.path.splitext(file_name)[1].lower()

        if ext in [".pdf"]:  # PDF Handling
            try:
                doc = fitz.open(file_name)
                for page_num, page in enumerate(doc):
                    # Try direct text extraction
                    page_text = page.get_text("text")
                    if page_text.strip():
                        extracted_text += page_text + "\n"
                    else:
                        # If no text, use OCR
                        img = page.get_pixmap()
                        image = Image.frombytes("RGB", [img.width, img.height], img.samples)
                        ocr_text = pytesseract.image_to_string(image)
                        extracted_text += ocr_text + "\n"
            except Exception as e:
                print(f"❌ Error processing PDF {file_name}: {e}")

        elif ext in [".png", ".jpg", ".jpeg"]:  # Image Handling
            try:
                image = Image.open(file_name)
                ocr_text = pytesseract.image_to_string(image)
                extracted_text += ocr_text + "\n"
            except Exception as e:
                print(f"❌ Error processing image {file_name}: {e}")

    # 🔹 Save Extracted Text
    output_file = "extracted_text.txt"
    if extracted_text.strip():
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(extracted_text)
        print(f"✅ Extracted text saved to '{output_file}'")
        print(f"🔹 First 1000 characters of extracted text:\n{extracted_text[:1000]}")
        files.download(output_file)  # Auto-download file
    else:
        print("⚠️ No text was extracted. Files might be empty or protected.")

