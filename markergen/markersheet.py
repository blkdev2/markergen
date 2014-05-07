from fpdf import FPDF
import simple
import pdfmarker

def thirty_simple_marker_sheet(start_id):
    """Create a PDF with 30 ARToolkitPlus 'simple' markers on a page.
    
    :param start_id: The ID number of the first marker on the sheet.
    """
    pdf = FPDF(unit="mm", format="letter")
    pdf.add_page()
    def draw_row(start_id, start_position):
        x_sp, y_sp = start_position
        for i in range(5):
            pattern = simple.SimplePattern(start_id + i)
            pdfmarker.draw_marker(pdf, pattern,
                                  (x_sp + i * 40, y_sp),
                                  (30, 30),
                                  5)
    for i in range(6):
        draw_row(start_id + i * 5, (12, 20 + 40 * i))
    return pdf

if __name__ == "__main__":
    pdf = thirty_simple_marker_sheet(0)
    pdf.output("simple_0-29.pdf")
