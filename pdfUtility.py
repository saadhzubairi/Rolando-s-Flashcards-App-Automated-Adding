import PyPDF2
import os

# Replace 'your_pdf_file.pdf' with the path to your PDF file.
pdf_file_path = "C:\\Users\\saadh\\OneDrive\\Desktop\\GRE\\GRE 5lb Manhattan.pdf"

# Create a directory to save the extracted chapters.
output_directory = "C:\\Users\\saadh\\OneDrive\\Desktop\\GRE\\file.txt"
os.makedirs(output_directory, exist_ok=True)

def extract_chapters(pdf_path):
    i= 0    
    pdf = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    
    # Loop through each page in the PDF.
    for page_number in range(len(pdf.pages)):
        print("on page",i)
        i+=1
        page = pdf.pages[page_number]
        
        # Extract the text from the current page.
        text = page.extract_text()
        
        # Check if this page contains the start of a new chapter (you may need to customize this based on your PDF structure).
        if "Chapter" in text:
            # Extract the chapter title and remove any special characters.
            chapter_title = text.strip().split('\n')[0]
            chapter_title = "".join(char for char in chapter_title if char.isalnum() or char.isspace())
            
            # Define the output file path for this chapter.
            chapter_file_path = os.path.join(output_directory, f'{chapter_title}.txt')
            
            # Write the chapter content to the text file.
            with open(chapter_file_path, 'w', encoding='utf-8') as chapter_file:
                chapter_file.write(text)

if __name__ == '__main__':
    extract_chapters(pdf_file_path)
