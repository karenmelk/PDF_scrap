import fitz  

pdf_path = 'test_task.pdf'

def read_all_pdf_data(pdf_path):
    all_text = ""

    # Open the PDF file
    with fitz.open(pdf_path) as pdf_document:
        # Iterate through all pages
        
        page = pdf_document[0]

        # Extract text from the page
        page_text = page.get_text()

        # Append text to all text variable
        all_text += page_text
        
    # Creting list splitting by \n
    lines = all_text.strip().split('\n')
    # Get first element from list 
    current_key = lines[0].strip()
    result_dict = {}
    # Giving to dict key, first element of list first element is title
    result_dict[current_key] = {}
    for line in lines[1:]:

        if ':' in line:
            key, value = map(str.strip, line.split(':', 1))
            result_dict[current_key][key] = value
        else:
            result_dict[current_key][key] =result_dict[current_key][key] +line
    return result_dict

print(read_all_pdf_data(pdf_path))