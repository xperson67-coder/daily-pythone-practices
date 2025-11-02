"""
Text Analyzer - Simple Sentence Counter
Author:the viliam
Description:
    Reads a UTF-8 encoded text file, splits it into sentences,
    and writes a formatted report showing character count and byte size.
"""
import re
file_path_input = r"C:\Users\w\Desktop\py test doc.txt"
file_path_output = r"C:\Users\w\Desktop\output.txt"

#in and out file paths  
with open(file_path_input, 'r', encoding='utf-8') as file:
    data=file.read() 
    paked=re.split(r'[.!?,]+', data)
    # spliting text containing characters .?!@3$"'; etc"  
    with open(file_path_output, 'w', encoding='utf-8') as out:
    #writng rep on  ourt put file 
        for index, steps in enumerate(paked , start=1):
        #returning index number and the item 
            if not steps.strip(): 
              continue 
            # Check if the step is not just whitespace
            ch_length=len(steps.encode('utf-8')) 
            #length of each item 
            ch_count=len(steps) 
            #count of each item 
           
            
            out.write( 
    f"""
    ---------------------
    Report for line {index}
    Character count: {ch_count}
    UTF-8 size: {ch_length} bytes
    Content:
    {steps}
    ---------------------
    """)
            print('Done!   ')
           
        
   