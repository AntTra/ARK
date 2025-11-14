# Klag til Anton, bare ikke gjør det mens jeg er full:)


###########################################################

#   Bingo-list theme can be changed at the bottom of the document

#   Use pyinstaller to update the Bingo.exe app or run the script manually (run the program, open bingo_sheets.pdf on the desktop, print it out, fetch the papers from your closest printer, use bingo)
    # Run this in terminal (be in desktop ('cd desktop'))
    # 1.   pyinstaller --onefile C:\Users\ARK\Desktop\Bingo.py
    # 2.   pyinstaller Bingo.spec
    # 3.   Check where the "dist" folder is located and move the Bingo.exe app to desktop    

#   The generated pdf itself is located in the desktop cuz Im lazy

#   Doesn't currently work with linux cuz os lib is a bitch n Im lazy. Just comment that line out and use manually

########################################################### 


# TODO: change fonts mayhaps? Helvetica is a hellish babe

from datetime import date
import random
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import simpleSplit
import numpy as np
import pandas as pd

import tempfile
import win32api
import win32print

#from django.conf import settings
#reportlab.rl_config.TTFSearchPath.append(str(settings.BASE_DIR) + '/app/lib/reportlabs/fonts')
#pdfmetrics.registerFont(TTFont('Copperplate', 'Copperplate-Gothic-Bold.ttf'))

def create_bingo_sheet(c, texts, x_offset, y_offset):
    cell_size = 78
    grid_size = 5
    text_padding = 5
    max_text_width = cell_size - 4 * text_padding
    c.setFont('Helvetica', 9)
    #current_date = date.today()

    for row in range(grid_size):
        for col in range(grid_size):
            x = x_offset + col * cell_size
            y = y_offset - row * cell_size
            c.setStrokeColor(colors.black)
            c.rect(x, y, cell_size, cell_size, fill=0)

            if row == 2 and col == 2:  
                c.drawString(x + text_padding, y + cell_size - text_padding - 12, "Full person")
            else:
                index = row * grid_size + col
                if index > (grid_size * grid_size) // 2:
                    index -= 1  
                text = texts[index]
                wrapped_text = simpleSplit(text, 'Helvetica', 9, max_text_width)
                text_y = y + cell_size - text_padding - 12

                for line in wrapped_text:
                    c.drawString(x + text_padding, text_y, line)
                    text_y -= 12  

def generate_bingo_pdf(filename, full_text_list):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter  
    img_file = "C:/Users/ARK/Pictures/arklogo_clean.png"

    for PDF_pages in range(5):        
        selected_texts = random.sample(full_text_list, 50)
        texts1 = selected_texts[:24]  
        texts2 = selected_texts[25:49] 

        c.drawImage(img_file, width / 7 - 90, height / 10.5 - 78 / 2, width = 120, preserveAspectRatio = True, mask = 'auto')
        c.drawImage(img_file, width - 105, height / 10.5 - 78 / 2, width = 120, preserveAspectRatio = True, mask = 'auto')
        c.drawImage(img_file, width / 7 - 90, height / 10.5 - height / 2 - 78 / 2, width = 120, preserveAspectRatio = True, mask = 'auto')
        c.drawImage(img_file, width - 105, height / 10.5 - height / 2 - 78 / 2, width = 120, preserveAspectRatio = True, mask = 'auto')

        create_bingo_sheet(c, texts1, 120, height - 80)
        create_bingo_sheet(c, texts2, 120, height / 2 - 80)

        c.showPage() 



    c.save()
    
    defaultPrinter = win32print.GetDefaultPrinter()
    if defaultPrinter != 'Brother HL-1210W series Printer':
        win32print.SetDefaultPrinter('Brother HL-1210W series Printer')
    path = os.path.join("C:/Users/ARK/Desktop/bingo_sheets.pdf")
    #print("Printing " + str(path) + " on " + str(win32print.GetDefaultPrinter()))
    win32api.ShellExecute(0, "print", os.path.join("C:/Users/ARK/Desktop/bingo_sheets.pdf"), None,  ".",  0)

    #os.startfile("curl parrot.live")

filename = r'C:\Users\ARK\Desktop\bingo_sheets.pdf'
assert os.path.isfile(filename)
with open(filename, "r") as f:
    pass
df = pd.read_excel('C:/Users/ARK/Desktop/Bingoliste.xlsx', sheet_name='Sheet2')
bingo_list = df[df.columns[0]].tolist()
generate_bingo_pdf(filename, bingo_list)

