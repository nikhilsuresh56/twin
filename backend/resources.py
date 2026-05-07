from pypdf import PdfReader
import pdfplumber 
import json

# Read LinkedIn PDF with tables
try:
    linkedin_parts = []
    
    with pdfplumber.open("./data/linkedin.pdf") as pdf:
        for page in pdf.pages:
            # Get text
            text = page.extract_text()
            if text:
                linkedin_parts.append(text)
            
            # Get tables
            tables = page.extract_tables()
            if tables:
                for table in tables:
                    if table:
                        for row in table:
                            if row:
                                linkedin_parts.append(" | ".join(str(cell) for cell in row if cell))
    
    linkedin = "\n".join(linkedin_parts)
    
except FileNotFoundError:
    linkedin = "LinkedIn profile not available"

# Read other data files (unchanged)
with open("./data/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()

with open("./data/style.txt", "r", encoding="utf-8") as f:
    style = f.read()

with open("./data/facts.json", "r", encoding="utf-8") as f:
    facts = json.load(f)

