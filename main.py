import os
import re
from fpdf import FPDF

# lists all files in the files dir
list_of_files = os.listdir(f"{os.getcwd()}\\files")
def extractUniqueNumber(content):
    pattern = re.compile(r'\{1[:]F[A-Z0-9]+')
    matches = pattern.findall(content)
    return  matches[0][4::]



def extractNumber(content):
    #\{2[:]O\d{3}
    pattern = re.compile(r'\{2\WO\d{3}')
    matches = pattern.findall(content)
    return  matches[0][4::]

def getContent(file_n):

    file = open(f"./files/{file_n}", "r")
    c = file.read()
    file.close()
    return c


def generatePDF(file_name, cont):
    # instanciate use of fpdf
    pdf = FPDF('P', 'mm', "Letter")
    pdf.set_auto_page_break(True)
    pdf.add_page()
    pdf.set_line_width(0.1)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(w= 180, h=10, txt = cont, border = 0, align='L', fill= False)
    pdf.output(f"{file_name}.pdf")


def divideIntoParts(file):
    pattern = re.compile(r'\{S[:]\{COP[:]S\}\}')
    c = getContent(file)
    matches = pattern.finditer(c)

    index_of_Last = [0]
    for mtches in matches:
        index_of_Last.append(mtches.span()[1])
    for i in range(0, len(index_of_Last)):
        if index_of_Last[i] != index_of_Last[-1]:
            content = c[index_of_Last[i]: index_of_Last[i + 1]].strip()
            file_name = extractNumber(content) +"-"+ extractUniqueNumber(content)
            generatePDF(file_name, content)



for file in list_of_files:
    divideIntoParts(file)
    print("done")
    content = getContent(file)
    extractUniqueNumber(content)
    fileName = extractNumber(content)
    generatePDF(fileName, content)

# file = open("./test.txt", "r")
# c = file.read()

#\{S[:]\{COP[:]S\}\}

