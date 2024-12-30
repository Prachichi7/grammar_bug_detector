import language_tool_python
import PyPDF2
from PyPDF2 import PdfReader

tool= language_tool_python.LanguageTool('en-US')

pdf_path= input("please enter the path of the pdf file you want to check:  ")
#or directly we can add the path of the pdf to the pdf_path

pdf_text= " "
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    pdf_text= " "
    for page in reader.pages:
        pdf_text += page.extract_text() + "\n"
    return pdf_text

def check_text(pdf_text, tool):
    matches= tool.check(pdf_text)
    return matches

def correction(matches):
    for match in matches:
        print(f"Issue: {match.message}")
        print(f"Suggestion: {', '.join(match.replacements)}")

def text_into_line():
    reader = PdfReader(pdf_path)
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if not text.strip():
            continue# Skip empty pages
    
    # Split text into lines
    lines = text.splitlines()
    for line_number, line in enumerate(lines, start=1):
        matches = tool.check(line)
        if matches:  # If issues found in the line
            for match in matches:
                print(f"Page {page_number}, Line {line_number}:")
                print(f"Issue: {match.message}")
                print(f"Suggestion: {', '.join(match.replacements)}\n")

def print_issues(pdf_path, tool):
    print(f"Analyzing PDF: {pdf_path}")
    pdf_text = extract_text_from_pdf(pdf_path) # Extract text from the PDF
    matches = check_text(pdf_text, tool)  # Check grammar
    correction(matches) 
    text_into_line()

print_issues(pdf_path, tool)

