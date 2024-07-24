from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Add image at coordinates (10, 70) with width of 190 mm
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "", 58)
        # Full page width, 57 height
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        # Line break of 20 units to move to the next line
        self.ln(20)


def shirtificate(shirt):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="A4")
    pdf.set_font("helvetica", size=40)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 213, f"{shirt} took CS50!", align="C")
    pdf.output("shirtificate.pdf")


def main():
    name = input("Name: ")
    shirtificate(name)




if __name__ == "__main__":
    main()
