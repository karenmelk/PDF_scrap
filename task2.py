import  regex_func # My written regex 
import fitz 

main_pdf = 'test_task.pdf'
your_pdf_for_compare = "path to your pdf for compare"
# Read all pdf data function for get data from PDF,add them to list and return 
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
        

    # return all_text
    lines = all_text.split('\n')
    return lines
# Compare structure is a function that return is given 2 data structures are same or not
def compare_structure(list1,list2):
    b = True
    # ZIP for two lists
    for i , j in zip(main_list,compare_list):
        if b == False:
            break
        # Check if i or j NONE data then pass this
        if len(i.strip()) == 0 and len(j.strip()) ==0:
            continue
        # Check if i or j have ':' symbol if no continue it can be contain text and for structure is not important
        elif (':' not in i) and (':' not in j):
            continue
        # Create variables key1 key2 and value2 

        key1 = i.split(':')[0].strip()
        key2 = j.split(':')[0].strip()
        value2 = j.split(':')[1].strip()
        # Check if key1 is equal key2 structure is ok 
        if key1 != key2:
            b = False
            break
        # Checking regex by: in regex_func file I write code for check patterns
        elif key1 == 'PN' or key1 =='MFG' or key1 == 'CERT SOURCE':
            b = regex_func.lower_case(value2)
        elif key1 == "DESCRIPTION" or key1 == 'CONDITION' or key1 == 'UOM':
            b = regex_func.upper_case(value2)
        elif key1 == 'LOCATION' or key1 == 'RECEIVER#' or key1 == 'BATCH#' or key1 == 'Qty' or key1 == 'SN' or key1 == 'LOT':
            b = regex_func.digits(value2)
        elif key1 == 'EXP DATE' or key1 == 'REC.DATE' or key1 == 'DOM':
            b = regex_func.date_case(value2)
        elif key1 == 'PO':
            b = regex_func.po(value2) 
    return b

main_list = read_all_pdf_data(main_pdf)
compare_list = read_all_pdf_data(your_pdf_for_compare)

print(compare_structure(main_list,compare_list))