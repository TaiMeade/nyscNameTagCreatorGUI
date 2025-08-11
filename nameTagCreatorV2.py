# Tai Meade
# Name tag creator for science camp
# 06/11/25

# sources used:
# https://www.geeksforgeeks.org/creating-pdf-documents-with-python/
# https://www.geeksforgeeks.org/python/python-read-csv-columns-into-list/

# importing modules
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.units import inch
import math
import sys
from typing import List
import requests
from pandas import read_csv

# Convert appropriate columns using a .csv file (retrieved from Airtable)
# Legal First Name - firstNames
# Preferred Private First Name - preferredFirstNames
# Legal Last Name - lastNames
# Delegate location - states
def colIntoList(fileName, columnName):
    data = read_csv(f"{fileName}.csv")
    return data[columnName].tolist()

# Checks to see if 3 lists have the same length
def allSameLength(list1, list2, list3):

    # checks if the 3 lists have the same length
    if (len(list1) != len(list2)) or (len(list2) != len(list3)):
        print("Unmatched number of first names, last names, and states.")
        print("Exiting program.")
        return False
    else:
        print("Input data sizes match. Pdf generating...")
        return True # returns true if they are all 3 same length
    
# clean any number of lists of their whitespace and NaN values
def cleanLists(*args: List):
    for list in args:
        for index, item in enumerate(list):
            if (type(item) == float):
                list[index] = ""
            else:
                item.strip()

# check if numNameTagRows is odd and if oddNum flag is set
def isLastAndOdd(i, numNameTagRows, flag):
    if (i == (numNameTagRows - 1.5) and flag):
        return True

inputFile = input("Enter the name of the input file: ")


firstNamesCol = colIntoList(inputFile, "Legal First Name")
preferredFirstNames = colIntoList(inputFile, "Preferred Private First Name")
lastNames = colIntoList(inputFile, "Legal Last Name")
states = colIntoList(inputFile, "Delegate location")

# Create firstNames using Preferred First Name where possible and
# Legal First Name otherwise
firstNames = []

for i in range(len(firstNamesCol)):
    if (type(preferredFirstNames[i]) == float):
        firstNames.append(firstNamesCol[i])
    else:
        firstNames.append(preferredFirstNames[i])

if allSameLength(firstNames, lastNames, states):
    nameOfFile = input("Enter the name of the output file: ")
else:
    sys.exit()

# clean the names and states of whitespace and floats (AKA NaN)
cleanLists(firstNames, lastNames, states)

# initializing variables with values
fileName = f'{nameOfFile}.pdf'
documentTitle = nameOfFile
image = 'image.png'

# creating a pdf object
pdf = canvas.Canvas(fileName)

x = 0.75 * inch # initial x coordinate for drawing the left rectangle
y = 9 * inch # initial y coordinate for drawing the right rectangle
width = 3.25 * inch # width of each nametag
height = 2 * inch # height of each nametag

rightX = 4 * inch # initial x coordinate for drawing the right rectangle

leftImageX = 0.90277777 * inch  # x for drawing the left image
imageY = 9.861111111 * inch     # initial y for drawing the image
rightImageX = 4.16666667 * inch # x for drawing the right image

numNameTagRows = len(firstNames) / 2
oddNum = False # flag for when there is an odd number of delegates...used to prevent drawing an extra nametag

# for when there is an odd number of delegates
if (numNameTagRows % 1 != 0):
    numNameTagRows += 1
    oddNum = True

# create the name tags...add 1 because of how range() works
for i in range(int(numNameTagRows)):

    # create a new page and reset appropriate coordinates
    if ((i % 5 == 0 and i != 0)):
        pdf.showPage()
        y = 9 * inch
        imageY = 9.861111111 * inch

    # draw the rectangles that go around the name tags
    pdf.rect(x,y, width, height, stroke=1, fill=0)

    # check if on last iteration and there if an odd number of delegates
    if not isLastAndOdd(i, numNameTagRows, oddNum):
        pdf.rect(rightX, y, width, height, stroke=1, fill=0)

    # draw the blue rectangles
    # check if on last iteration and there if an odd number of delegates
    if isLastAndOdd(i, numNameTagRows, oddNum):
        pdf.setFillColor(colors.blue)
        pdf.rect(x, y + (0.6 * inch), width, 0.1 * inch, stroke=1, fill=1)
        pdf.rect(x, y + (0.1 * inch), width, 0.1 * inch, stroke=1, fill=1)
    else:
        pdf.setFillColor(colors.blue)
        pdf.rect(x, y + (0.6 * inch), width * 2, 0.1 * inch, stroke=1, fill=1)
        pdf.rect(x, y + (0.1 * inch), width * 2, 0.1 * inch, stroke=1, fill=1)

    # subtract offset for height of namecards (2 inches)
    y -= height
    
    # draw the image at appropriate spots
    pdf.drawInlineImage(image, leftImageX, imageY)

    # check if on last iteration and there if an odd number of delegates
    if not isLastAndOdd(i, numNameTagRows, oddNum):
        pdf.drawInlineImage(image, rightImageX, imageY)

    # draw the "National Youth Science Camp" on left nametags
    text = pdf.beginText(1.25 * inch, imageY - (.4166666667 * inch))
    text.setFont("Courier", 10)
    text.setFillColor(colors.black)
    text.textLine("National Youth Science Camp")
    pdf.drawText(text)

    # draw the "National Youth Science Camp" on right nametags
    # check if on last iteration and there if an odd number of delegates
    if not isLastAndOdd(i, numNameTagRows, oddNum):
        rightText = pdf.beginText(4.513888889 * inch, imageY - (.4166666667 * inch))
        rightText.setFont("Courier", 10)
        rightText.setFillColor(colors.black)
        rightText.textLine("National Youth Science Camp")
        pdf.drawText(rightText)

    # draw delegate information
    try:
        # draw their state
        pdf.setFont("Courier-BoldOblique", 10)
        pdf.setFillColor(colors.black)
        pdf.drawCentredString(2.35 * inch, imageY - (0.59 * inch), states[i])
        
        # check if on last iteration and there if an odd number of delegates
        if not isLastAndOdd(i, numNameTagRows, oddNum):
            pdf.drawCentredString(2.35 * inch + width, imageY - (0.59 * inch), states[len(states) - i - 1])

        # draw their first names
        if (len(firstNames[i]) > 15):
            pdf.setFont("Courier-Bold", 14)
        elif (len(firstNames[i]) > 12):
            pdf.setFont("Courier-Bold", 16)
        elif (len(firstNames[i]) < 7):
            pdf.setFont("Courier-Bold", 24)
        else:
            pdf.setFont("Courier-Bold", 20)

        pdf.drawCentredString(2.9 * inch, imageY + (0.6 * inch), firstNames[i])
        
        if not isLastAndOdd(i, numNameTagRows, oddNum):
            if (len(firstNames[len(firstNames) - i - 1]) > 15):
                pdf.setFont("Courier-Bold", 14)
            elif (len(firstNames[len(firstNames) - i - 1]) > 12):
                pdf.setFont("Courier-Bold", 16)
            elif (len(firstNames[len(firstNames) - i - 1]) < 7):
                pdf.setFont("Courier-Bold", 24)
            else:
                pdf.setFont("Courier-Bold", 20)
            pdf.drawCentredString(2.9 * inch + width, imageY + (0.6 * inch), firstNames[len(firstNames) - i - 1])

        # draw their last names
        pdf.setFont("Courier", 10)
        pdf.drawCentredString(2.9 * inch, imageY + (0.25 * inch), lastNames[i])
        
        if not isLastAndOdd(i, numNameTagRows, oddNum):
            pdf.drawCentredString(2.9 * inch + width, imageY + (0.25 * inch), lastNames[len(lastNames) - i - 1])

    except Exception as e:
        print(e)

    # subtract offset from the y 
    imageY -= height

    

# setting the title of the document
pdf.setTitle(documentTitle)

# saving the pdf
pdf.save()
print("Pdf successfully generated and saved.")