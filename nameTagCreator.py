# Tai Meade
# Name tag creator for science camp
# 06/11/25

# sources used:
# https://www.geeksforgeeks.org/creating-pdf-documents-with-python/

# importing modules
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.units import inch
import math
import sys

firstNames = "Tina,Vineet,Grace,Manning,Vieve,Katherine Emily,Prisha,Joseph,Sindia,Irene,Mary,Susie,Jyotsna,Laasya,Grace,Sudipa,Khai,Emma,Nikolai,Samantha,Gemma,Bryan,Jeemin,Annabella,Atchaya,Carson,Kris,Antariksha,Mia Sakata,Leena,Rayan Mahdi,Emmalee,Fe,Anika,Thomas,Austin,Elijah,Alayna,Sophia,Eric,Vyshnavi,John,Madeline,Mary,Vikram,Andy,Savannah,Jessica,Sahiba,Kinzey,Mason Alexander,Lucas,Naomi,Andre,Gideon,Camille,Carolyn,Julia,Elisea Amara,Holly,Mai,Solomon,Angelina,Jahnavi,Brooks,James,Kyla,Sophie,Joseph,Sophia,Bristol,Lucia,Mateen,Tiffany,Milo,Sadie Olivia,Enoch Jiang,Jane,Joseph,Carter,Imre,Ike,Michael,Benjamin,Mariam,Griffin,Arushi,Breanne Grace,Gabi,Isabelle,Elizabeth,Max,Aidan,Cecilia,Matthew,Emberlynn,Jackson,Gastón Gabriel,Giuliana,Gabriela Guadalupe,Giovana,Marty,Sofi,Nicole,Azul Kamilah,Jorge,Marian,Noel Armando,Akash,Danielle,Vaishnava".split(",")
lastNames = "Gao,Vadrevu,Muldoon,Zhang,Muldoon,Lam,Shroff,Chen,Michael,Pan,Orji,Blackford,Venkat,Chintapalli,Yang,Chowdhury,Matsudaira,Colarte Delgado,Pratasenia,Dalby,Muller-Smit,Li,Kim,Liutikas,Muthupalaniappan,Fu,Lau,Sharma,Stogdill,Dudi,Zaman,Otipoby,Berling,Chegireddy,Gershanik,McConkey,Bouchard,Hu,Li,Zhou,Donthabhaktuni,Saleeby,Awad,Zins,Sharma,Chen,Massey,Wu,Kaur,Clark,Mickelson,Askew,Long,Lee,Shalev,Branch,He,Huang,Jackson,Steen,Tran,Blecher,Li,Kari,Beyer,Gessey,Fallis,Wu,Wang,Xia,Hill,Williams,Hasan,Wang,Baumgartner,McCann,Jiang,Zheltov,Michna,Wildrick,Barna,Sowemimo,Gearing,Chiu,Doucoure,Hengelsberg,Raizada,Graham,Carrasco,Moosman,Kinghorn,Chen,Ward,King,Oimoen,Thompson,Darin,Diaz,Lodolo,Ledezma Hidalgo,Rocha Dos Santos,Contreras Jara,Pavez García,Martínez González,Hernandez Hernandez,Ibarra Flores,Suárez Agrazal,Espinosa Santamaría,Ragoo,Franklyn,Ramjass".split(",")
states = "Alabama,Alabama,Alaska,Alaska,Alaska,Arizona,Arizona,Arkansas,Arkansas,California,California,Colorado,Connecticut,Connecticut,Delaware,Delaware,District of Columbia,Florida,Florida,Georgia,Hawaii,Idaho,Idaho,Illinois,Illinois,Indiana,Indiana,Iowa,Iowa,Kansas,Kansas,Kentucky,Kentucky,Louisiana,Louisiana,Maine,Maine,Maryland,Maryland,Massachussets,Massachussets,Missouri,Missouri,Minnesota,Minnesota,Mississippi,Mississippi,Michigan,Michigan,Montana,Montana,Nebraska,Nebraska,Nevada,Nevada,New Hampshire,New Jersey,New Jersey,New Mexico,New Mexico,New York,New York,North Carolina,North Carolina,North Dakota,North Dakota,Ohio,Ohio,Oklahoma,Oklahoma,Oregon,Oregon,Pennsylvania,Pennsylvania,Rhode Island,Rhode Island,South Carolina,South Carolina,South Dakota,Tennessee,Tennessee,Texas,Texas,Utah,Utah,Vermont,Virginia,Virginia,Washington,Washington,West Virginia,West Virginia,Wisconsin,Wisconsin,Wisconsin,Wyoming,Wyoming,Argentina,Argentina,Bolivia,Brazil,Chile,Chile,Costa Rica,Mexico,Mexico,Panama,Panama,Trinidad and Tobago,Trinidad and Tobago,Trinidad and Tobago".split(",")
fullNames = []

if (len(firstNames) != len(lastNames)) or (len(lastNames) != len(states)):
    print("Unmatched number of first names, last names, and states.")
    print("Exiting program.")
    sys.exit()
else:
    # prompt user for name of the file they are creating/generating
    nameOfFile = input("Name of file you create: ")
    print("Input data sizes match. Pdf generating...")

# clean the names and states of whitespace
for name in firstNames:
    name.strip()

for name in lastNames:
    name.strip()

for state in states:
    state.strip()

for i in range(len(firstNames)):
    fullNames.append(firstNames[i] + " " + lastNames[i])


# for i in range(len(firstNames)):
#     print(firstNames[i], lastNames[i], states[i])

# for name in fullNames:
#     print(name)

# initializing variables with values
fileName = f'{nameOfFile}.pdf'
documentTitle = nameOfFile
image = 'image.png'

# creating a pdf object
pdf = canvas.Canvas(fileName)

x = 0.75 * inch
y = 9 * inch
width = 3.25 * inch
height = 2 * inch

rightX = 4 * inch

leftImageX = 0.90277777 * inch
imageY = 9.861111111 * inch
rightImageX = 4.16666667 * inch

yOffset = 2 * inch
xOffset = 3.25 * inch

numNameTagRows = len(firstNames) / 2

# for when there is an odd number of delegates
if (numNameTagRows % 1 != 0):
    numNameTagRows += 1
print(int(numNameTagRows))
# create the name tags...add 1 because of how range() works
for i in range(int(numNameTagRows)):

    # create a new page and reset appropriate things
    if ((i % 5 == 0 and i != 0)):
        pdf.showPage()
        y = 9 * inch
        imageY = 9.861111111 * inch

    # draw the rectangles that go around the name tags

    pdf.rect(x,y, width, height, stroke=1, fill=0)
    pdf.rect(rightX, y, width, height, stroke=1, fill=0)

    # draw the blue rectangles
    pdf.setFillColor(colors.blue)
    pdf.rect(x, y + (0.6 * inch), width * 2, 0.1 * inch, stroke=1, fill=1)
    pdf.rect(x, y + (0.1 * inch), width * 2, 0.1 * inch, stroke=1, fill=1)

    # subtract offset for height of namecards (2 inches)
    y -= height
    
    # draw the image at appropriate spots
    pdf.drawInlineImage(image, leftImageX, imageY)
    pdf.drawInlineImage(image, rightImageX, imageY)

    # draw the "National Youth Science Camp" on left nametags
    text = pdf.beginText(1.25 * inch, imageY - (.4166666667 * inch))
    text.setFont("Courier", 10)
    text.setFillColor(colors.black)
    text.textLine("National Youth Science Camp")
    pdf.drawText(text)

    # draw the "National Youth Science Camp" on right nametags
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
        pdf.drawCentredString(2.35 * inch + xOffset, imageY - (0.59 * inch), states[len(states) - i - 1])

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

        if (len(firstNames[len(firstNames) - i - 1]) > 15):
            pdf.setFont("Courier-Bold", 14)
        elif (len(firstNames[len(firstNames) - i - 1]) > 12):
            pdf.setFont("Courier-Bold", 16)
        elif (len(firstNames[len(firstNames) - i - 1]) < 7):
            pdf.setFont("Courier-Bold", 24)
        else:
            pdf.setFont("Courier-Bold", 20)
        pdf.drawCentredString(2.9 * inch + xOffset, imageY + (0.6 * inch), firstNames[len(firstNames) - i - 1])

        # draw their last names
        pdf.setFont("Courier", 10)
        pdf.drawCentredString(2.9 * inch, imageY + (0.25 * inch), lastNames[i])
        pdf.drawCentredString(2.9 * inch + xOffset, imageY + (0.25 * inch), lastNames[len(lastNames) - i - 1])

    except:
        print("err")

    # subtract offset from the y 
    imageY -= yOffset

    

# setting the title of the document
pdf.setTitle(documentTitle)

# creating the title by setting it's font 
# and putting it on the canvas
pdf.setFont('Courier', 36)

# creating a multiline text using
# textline and for loop
# text = pdf.beginText(40, 680)
# text.setFont("Courier", 18)
# text.setFillColor(colors.red)

# for line in textLines:
#     text.textLine(line)
    
# pdf.drawText(text)

# saving the pdf
pdf.save()
print("Pdf successfully generated and saved.")