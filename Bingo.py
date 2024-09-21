# Vovanoja. In other words, may contain cursing in the notes

###########################################################

#   Bingo-list theme can be changed at the bottom of the document

#   Use pyinstaller to update the Bingo.exe app or run the script manually (run the program, open bingo_sheets.pdf on the desktop, print it out, fetch the papers from your closest printer, use bingo)
    # Run this in terminal
    # 1.   pyinstaller --onefile C:\Users\ARK\Desktop\Bingo.py
    # 2.   pyinstaller Bingo.spec
    # 3.   Check where the "dist" folder is located and move the Bingo.exe app to desktop    

#   The generated pdf itself is located in the desktop

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

        c.drawImage(img_file, width / 7 - 90, height / 10.5 - 78 / 2, width=120, preserveAspectRatio=True, mask='auto')
        c.drawImage(img_file, width - 105, height / 10.5 - 78 / 2, width = 120, preserveAspectRatio=True, mask='auto')
        c.drawImage(img_file, width / 7 - 90, height / 10.5 - height / 2 - 78 / 2, width=120, preserveAspectRatio=True, mask='auto')
        c.drawImage(img_file, width - 105, height / 10.5 - height / 2-78 / 2, width=120, preserveAspectRatio=True, mask='auto')

        create_bingo_sheet(c, texts1, 120, height - 80)
        create_bingo_sheet(c, texts2, 120, height / 2 - 80)

        c.showPage() 

    c.save()
    os.startfile("C:/Users/ARK/Desktop/bingo_sheets.pdf", "print")

###########################################################

#   Add bingo texts under here, but add em alphabetically pls ffs

###########################################################

standard_bingo_texts = [ 
"'Hvor er bodegaen?'", 
"'Det er bare vann'",	
"'Det er meg altså'",		
"'Er det noe bra her?'",		
"'Er dette lysssshe?'",		
"'Hvor er [Lokalet personen står i]?'",		
"'Hvor er doen?'",
"'Jeg har stempel'",		
"'Jeg kan hjelpe til med bingoen'",		
"'Enda et stempel?'",		
"'Jeg skal bare se om det er noen her'",		
"'Kommer jeg ut her?'",		
"'Legg' på telefonen",		
"'Må JEG vise leg?'",		
"'Ser bilde falskt ut?'",		
"'Skjegg er jo legg'",		
"'Legget mitt er inne i lokalet'",		
"'Åh, har dere bingo?'",		
"Bli med på KSGs stilletime",		
"Blar gjennom minst 3 kort",		
"Du blir forsøkt sjekket opp",		
"Du bruker 10 sekunder på å studere legg til en over 30",		
"Du får et merkelig kompliment",		
"Du gir veibeskrivelse til noen som aldri kommer til å klare å følge",		
"Du hører på sambandet at noen har spydd på huset",		
"Du må forklare hvor doen er",		
"Du får tilbud om virgins", 		
"Du spør en KSG om de vil ha godteri (Du trenger ikke gi bort noe)",		
"Du sjekker legg på en person du vet er over 20",		
"Du spør noen som er på jobb om legg, uheldigvis",		
"Flekser armen når de får/viser stempel",		
"Folk som bare vil ha stempel og så går",		
"For en-inn-en-ut: De i køen har bedre kontroll enn deg",		
"Forlater de under 20år",		
"Du får en klem av en gammel venn",		
"Full ARKer",		
"Full person henger med leggsjekken",		
"Gamle husfolk på byen",		
"Gammel kjenning",		
"Gi en vakt en high-five",		
"Gjengkort eller medlemskort som aldersbevis",		
"Går inn i lokalet etter 0200",		
"Har legg i jakken i garderoben",		
"Har tatovering så det er vanskelig å stemple",		
"Heller ut drikke når de får stempel",		
"Fylt 20 for en time siden",		
"Internasjonal legitimasjon",		
"Kjenner bartenderne/ DJ",		
"Klager over for mange stempel",		
"Klager på musikken",		
"Klager på planløsning",		
"Kort i BH'en",		
"Krangler for en venn som ikke er 20 / ikke har med legg",		
"Krangler fordi de ikke får ta med sprit ut",		
"Legger person født før 1984",		
"Legger seg inn for å gå på do",		
"Leggsjekkere vedder noe på hvem som vinner bingo",		
"Livet ditt blir beriket av Tormods nærvær",		
"Nekter å bruke garderoben",		
"Noen er sure fordi du ikke husker dem",		
"Noen går inn og rett ut igjen",		
"Noen har 'glemt' leggen i jakka",		
"Noen har kledd seg ut",		
"Noen har på seg dress / lang kjole",		
"Noen har på seg kostyme, men det er ikke temafest på huset",		
"Noen har åpenbart gått feil vei og må snu",		
"Noen kliner før 0100",		
"Noen lar den ene i gjengen som ikke er 20 bli igjen",		
"Noen mister kort på gulvet",		
"Noen prøver å hjelpe til med bingoen ved å lese dette",		
"Noen prøver å ta med sprit ut",		
"Noen på jobb som viser legg",		
"Noen skal tydelig gå hjem sammen",		
"Noen som ber om godteri",		
"Noen som har glemt eller 'glemt' legg",		
"Noen som mener studiebevis burde fungere som legg",		
"Noen som stopper for å snakke, men går ikke inn",		
"Noen spør om veien til hyblene",		
"Noen står alene og loker med mobilen",		
"Noen tar det som et kompliment at du spør om legg",		
"Noen under 20 prøver å komme inn",		
"Noen viser feil stempel",		
"Overraska over at vi jobber frivillig",		
"Pass som legg",		
"Person du kjenner: 'Jobber du her!?'",		
"Person henger ikke fra seg jakka",		
"Person med øl",		
"Person som bare går rett inn",		
"Person tror du jobber i Radio Revolt",		
"Promper og går videre",		
"Prøver å 'smugle' ut øl",		
"Prøver å hjelpe til med bingoen",		
"Samfundetkort som legg",		
"Ser bakover mot køen når du sjekker legg",		
"Skal bare ha stempel, går ikke inn",		
"Smilende KSGer",		
"Smiler når du ser dem inn i øynene",		
"Snur i døra",		
"Spiser opp alt godteriet",		
"Spør om ARK",		
"Spør om du vil ha drikke",		
"Spør om du vil være med på konsert",		
"Spør om hva som skjer på huset",		
"Stopper rett på innsida av leggsjekkpost",		
"Stressa KSGer",		
"Styrter drinken fordi de ikke kan ta den med ut",		
"Tar godteri uten å spørre",		
"Tormod leser dette",		
"Tror vi er vakter",		
"Ung person påstår at det synes at hen er over 20",
"Vakt som stopper for smalltalk",		
"Vaktene melder fullt hus",		
"Vaktene må tørke spy",		
"Vekter prøver å hjelpe til med bingoen",
"Vil ha flere stempel",		
"Vil ikke ha stempel",		
"Vil tramp stamp (e)",		
"Du starter på din tredje kopp kaffe", 
"Viser feil stempel", 
"Viser leg / stempel på vei ut av lokalet", 
"Viser stempel på vei ut",]

verksted_bingo_texts = [ # Unsorted
"Fastnøkler",
"Loddebolt",
"Avbitere",
"El-teip",
"Loddetinn",
"Skiftenøkkel",
"Umbrakonøkkel",
"Coax-kabel",
"Førstehjelpsskrin",
"Papir",
"WD-40/annet smøremiddel",
"Tusj",
"Connectors til coax-kabler",
"Arbeidshansker",
"Hjelm",
"Coax-kabelkuttere",
"Oscilloskop",
"Ting ikke til utlån",
"EL-avfall",
"Kondensatorer",
"Ølkjøleskap",
"Pling!-tang/knapp",
"Variac/Variabel spennings- forsyning",
"Blårens",
"Støvsuger",
"Oddbjørn",
"Maling",
"Lommelykt",
"Utlånsbok",
"Attenuator",
"Motstander",
"Metallstøv",
"3D-printer",
"Saks",
"Banankabler",
"Målebånd",
"Rotekasse",
"Tau",
"Antenneanalysator",
"Multimeter",
"Window Master 2000",
"Bruksmanualer",
"Bor",
"Lithium-batteri",
"Renblåsingspistol",
"Lim",
"Brannfarlig avfall",
"Hørselsvern",
"Skjøteledninger",
"Induksjonsmotor",
"Kniv",
]

toga_bingo_texts = [ # Not done

]

halloween_bingo_texts = [ # Not done

]

gudenesnattes_bingo_texts = [ # Not done

]

filename = r'C:\Users\ARK\Desktop\bingo_sheets.pdf'
generate_bingo_pdf(filename, standard_bingo_texts)

