#Libraries
import pyttsx3
import PyPDF2


pdf_reader = PyPDF2.PdfReader(open("example_CV.pdf", "rb"))

speaker = pyttsx3.init()
# Cleaning text - to be improved
for page_number in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[page_number].extract_text()
    clean_text = text.strip().replace("\n", " ")
    # Printing to double check
    # print(clean_text)

speaker.save_to_file(clean_text, "CV.mp3")
speaker.runAndWait()
speaker.stop()