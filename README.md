### Text Analyzer
**Description:**  
A simple Python script that reads a text file, splits it into sentences, and reports the character count and byte size of each sentence.  

**How it works:**
1. Reads a UTF-8 encoded `.txt` file.
2. Splits the content by `.`, `!`, or `?`.
3. Writes a formatted report to a new `output.txt` file.

**What I learned:**
- File handling in Python (`open`, `with` context manager)
- String manipulation and sentence splitting
- UTF-8 encoding and character counting
- Writing formatted output files

**Usage:**
- Place your text file in the specified path.
- Run the Python script:
  ```bash
  python text_analyzer.py
