from fpdf import FPDF


def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.image("shirtificate.png", 0, -25, 190, 190)
    pdf.set_font("helvetica", "B", 25)
    pdf.set_text_color(255, 255, 255)
    pdf.text(45, 45, f"{name} took CS50")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
