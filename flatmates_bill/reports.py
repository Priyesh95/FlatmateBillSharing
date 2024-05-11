import webbrowser
import os
from fpdf import FPDF

class PdfReport:

    def __init__(self,filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        pdf.image("files/house.png", w=30, h=30)

        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates bill" , border=0, align="C", ln=1)
        
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:" , border=0)
        pdf.cell(w=150, h=40, txt=bill.period , border=0, ln=1)

        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name , border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate1.pays(bill,flatmate2))) , border=0, ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name , border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate2.pays(bill,flatmate1))) , border=0, ln=1)
        
        os.chdir('files')
        pdf.output(self.filename + '.pdf')
        # webbrowser.open('file://' + os.path.realpath(self.filename + '.pdf'))
