import fitz  # PyMuPDF
import json

def extract_bold_text(pdf_path):
    bold_words = []

    # Open the PDF
    doc = fitz.open(pdf_path)

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text_instances = page.get_text("dict")["blocks"]

        # Loop through the text instances
        for block in text_instances:
            if "lines" in block:  # Ensure it's a text block
                for line in block["lines"]:
                    for span in line["spans"]:
                        if "bold" in span["font"].lower():  # Check if the font style includes "bold"
                            bold_words.append(span["text"])
        
        bold_words = list(set(bold_words)) #Remove repeated words

        #List of words and characteresto be removed fromt he list
        to_remove = [' ', 'Street ', 'Wd Prec Dist PWD Zip ', '*',   '  Note;'] 

        bold_words = [i for i in bold_words if i not in to_remove]
        bold_words = [i for i in bold_words if len(i) > 8]
        bold_words = [i.split(',')[0] for i in bold_words]

    doc.close()
    return bold_words

# Usage
pdf_path = "../Crimes_In_Boston/PDF/street_names.pdf"
bold_text = extract_bold_text(pdf_path)

'''There is a text file that already has some street names that are not in the Streetbook, 
so we'll open it and update it with the streets in the Boston Streetbook.'''

#Open the txt file
file_r = open('../Crimes_In_Boston/Txt/boston_streetbook.txt', 'r')
streetbook = file_r.readlines()
streetbook = [line.replace(',\n', '').replace('\n', '') for line in streetbook]
file_r.close()

#Add the new list to the streetbook and sort the streets
streetbook += bold_text
streetbook.sort()

#Load a json file with misspelled street
file_j = open('../Crimes_In_Boston/Json_Files/misspelled_st.json', 'r')
misspelled_st = json.load(file_j)
file_j.close()

#Correct misspelled Street
for street in streetbook:
    if street in misspelled_st.keys():
        streetbook[streetbook.index(street)] = misspelled_st[street]


#Save in a text file
with open('../Crimes_In_Boston/Txt/streetbook.txt', 'w') as file:
    for street in streetbook:
        file.write(street+'\n')
    
    file.close()